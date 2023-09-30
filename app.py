import json

from flask import Flask, render_template, request, redirect, url_for, session
from grafo import Usuario
from utils import GrafoUsuarios
from arbol_binario import ArbolBinario
import networkx as nx
import matplotlib.pyplot as plt
import random

app = Flask(__name__)
app.secret_key = 'clave_secreta'

grafo_usuarios = GrafoUsuarios()
arbol = ArbolBinario()

usuario1 = Usuario("usuario1@example.com", "contraseña1", "Juan", "Pérez", 30, "Hombre")
usuario2 = Usuario("usuario2@example.com", "contraseña2", "María", "Gómez", 25, "Mujer")
usuario3 = Usuario("usuario3@example.com", "contraseña3", "Pedro", "Sánchez", 35, "Hombre")
usuario4 = Usuario("usuario4@example.com", "contraseña4", "Ana", "Martínez", 28, "Mujer")

# Definir intereses de usuarios
usuario1.agregar_interes("Deportes")
usuario1.agregar_interes("Tecnología")
usuario1.agregar_interes("Ciencia")

usuario2.agregar_interes("Cine")
usuario2.agregar_interes("Música")

usuario3.agregar_interes("Viajes")
usuario3.agregar_interes("Gastronomía")

usuario4.agregar_interes("Arte")
usuario4.agregar_interes("Ciencia")

# Agregar usuarios al grafo
grafo_usuarios.agregar_usuario(usuario1.correo, usuario1)
grafo_usuarios.agregar_usuario(usuario2.correo, usuario2)
grafo_usuarios.agregar_usuario(usuario3.correo, usuario3)
grafo_usuarios.agregar_usuario(usuario4.correo, usuario4)

# Agregar conexiones entre usuarios
grafo_usuarios.agregar_conexion(usuario1.correo, usuario2.correo)
grafo_usuarios.agregar_conexion(usuario2.correo, usuario3.correo)
grafo_usuarios.agregar_conexion(usuario3.correo, usuario4.correo)

# Agregar usuarios al árbol
arbol.agregar_objeto(usuario1, usuario1.generar_lista_binaria_intereses())
arbol.agregar_objeto(usuario2, usuario2.generar_lista_binaria_intereses())
arbol.agregar_objeto(usuario3, usuario3.generar_lista_binaria_intereses())
arbol.agregar_objeto(usuario4, usuario4.generar_lista_binaria_intereses())

json_file = "persona.json"
with open(json_file, mode='r') as file:
    data = json.load(file)


nodos_a_mostrar = 1500
grafito = nx.Graph()
i = 0
for registro in data:
    if(i<nodos_a_mostrar):
        grafito.add_node(registro['ID'])
        for seguido in registro['seguidosL']:
            grafito.add_edge(registro['ID'], seguido)
        i+=1


pos = nx.spring_layout(grafito)
nx.draw(grafito, pos, with_labels=True, node_size=10, font_color="black", font_size = 1)
etiquetas_aristas = nx.get_edge_attributes(grafito, "weight")
nx.draw_networkx_edge_labels(grafito, pos, edge_labels=etiquetas_aristas)
plt.show()




@app.route('/')
def wellcome():
    return render_template('wellcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['username']
        contraseña = request.form['password']
        global usuario_verificado
        usuario = grafo_usuarios.buscar_usuario_por_correo(correo)
        if usuario and usuario.contraseña == contraseña:
            usuario_verificado = usuario            
            return redirect(url_for('index'))
        else:
            error = 'Correo o contraseña incorrectos. Inténtalo de nuevo.'
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Obtiene los datos del formulario
        username = request.form['username']
        password = request.form['password']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        edad = request.form['edad']
        genero = request.form['genero']
        intereses = request.form.getlist('intereses[]')

        if grafo_usuarios.buscar_usuario_por_correo(username):
            error = 'El correo electrónico ya está registrado.'
            return render_template('signin.html', error=error)
            
        nuevo_usuario = Usuario(username, password, nombres, apellidos, edad, genero)
        nuevo_usuario.intereses= intereses
        grafo_usuarios.agregar_usuario(nuevo_usuario.correo,nuevo_usuario)     
                
        return redirect(url_for('login'))
    
    return render_template('signin.html')

@app.route('/index')
def index():  
    
    conexiones = grafo_usuarios.buscar_conexiones(usuario_verificado.correo)          
    recomendaciones = grafo_usuarios.recomendar_conexiones(usuario_verificado.correo)     
    coincidencias = arbol.buscar_objetos_por_lista_binaria(usuario_verificado.generar_lista_binaria_intereses())
    todas_las_recomendaciones = recomendaciones + coincidencias
    todas_las_recomendaciones = list(set(todas_las_recomendaciones))
    todas_las_recomendaciones = [recomendacion for recomendacion in todas_las_recomendaciones if recomendacion not in conexiones]
    global rec 
    rec = todas_las_recomendaciones
    if usuario_verificado in todas_las_recomendaciones:
     todas_las_recomendaciones.remove(usuario_verificado)
    return render_template('index.html', user=usuario_verificado, conexiones=conexiones, recomendaciones = todas_las_recomendaciones)

@app.route('/recomendaciones')
def mostrar_recomendaciones():    

    return render_template('recomendaciones.html', recomendaciones=rec)
    
@app.route('/agregar_conexion/<correo>')
def agregar_conexion(correo):

    grafo_usuarios.agregar_conexion(usuario_verificado.correo, correo)


    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

