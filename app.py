from flask import Flask, render_template, request, redirect, url_for, session
from grafo import Usuario
from utils import GrafoUsuarios, RedSocialArbol
from arbol_binario import ArbolBinario
from post import Post
import json
import random

app = Flask(__name__)
app.secret_key = 'clave_secreta'

grafo_usuarios = GrafoUsuarios()
arbol = ArbolBinario()
publicaciones = RedSocialArbol()

archivo_json = 'demo_persona.json'

# Leer el contenido del archivo JSON
with open(archivo_json, 'r') as archivo:
    datos_json = json.load(archivo)

# Iterar sobre los datos y crear objetos Usuario
for datos_persona in datos_json:
    correo = datos_persona["correo"]
    contraseña = datos_persona["contrasena"]
    nombres = datos_persona["nombre"]
    apellidos = datos_persona["apellido"]
    edad = int(datos_persona["edad"])
    genero = datos_persona["genero"]
    intereses = datos_persona["intereses"]

    nuevo_usuario = Usuario(correo, contraseña, nombres, apellidos, edad, genero)
    nuevo_usuario.intereses = intereses

    grafo_usuarios.agregar_usuario(nuevo_usuario.correo, nuevo_usuario)
    arbol.agregar_objeto(nuevo_usuario, nuevo_usuario.lista_binaria_intereses)   



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
grafo_usuarios.agregar_conexion(usuario1, usuario2)
grafo_usuarios.agregar_conexion(usuario2, usuario3)
grafo_usuarios.agregar_conexion(usuario3, usuario4)
grafo_usuarios.agregar_conexion(usuario4, usuario1)

# Agregar usuarios al árbol
arbol.agregar_objeto(usuario1, usuario1.lista_binaria_intereses)
arbol.agregar_objeto(usuario2, usuario2.lista_binaria_intereses)
arbol.agregar_objeto(usuario3, usuario3.lista_binaria_intereses)
arbol.agregar_objeto(usuario4, usuario4.lista_binaria_intereses)


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
    componentes = grafo_usuarios.componentes_conexos()
    print("Componentes Conexos:")
    for i, componente in enumerate(componentes, 1):
     print(f"Componente {i}: {componente}")

    conexiones = grafo_usuarios.buscar_conexiones(usuario_verificado.correo)          
    recomendaciones = grafo_usuarios.recomendar_conexiones(usuario_verificado.correo)     
    coincidencias = arbol.buscar_objetos_por_lista_binaria(usuario_verificado.lista_binaria_intereses)
    todas_las_recomendaciones = recomendaciones + coincidencias 
    todas_las_recomendaciones = list(set(todas_las_recomendaciones))
    todas_las_recomendaciones = [recomendacion for recomendacion in todas_las_recomendaciones if recomendacion not in conexiones]
    global seguidores 
    seguidores = usuario_verificado.seguidores
    global rec 
    rec = todas_las_recomendaciones
    if usuario_verificado in todas_las_recomendaciones:
     todas_las_recomendaciones.remove(usuario_verificado)
    return render_template('index.html', user=usuario_verificado, conexiones=conexiones, recomendaciones = todas_las_recomendaciones, seguidores = seguidores)

@app.route('/recomendaciones')
def mostrar_recomendaciones():    

    return render_template('recomendaciones.html', recomendaciones=rec, seguidores = seguidores)
    
@app.route('/agregar_conexion/<correo>')
def agregar_conexion(correo):

    grafo_usuarios.agregar_conexion(usuario_verificado.correo, correo)


    return redirect(url_for('index'))

@app.route('/crear_post', methods=['GET', 'POST'])
def crear_post():
    if request.method == 'POST':
        contenido = request.form['contenido']
        lista_binaria = usuario_verificado.generar_lista_binaria_intereses()  # Lista binaria del usuario actual
        post = Post(usuario_verificado, contenido)
        arbol.agregar_objeto(post, lista_binaria)

        return redirect(url_for('index'))

    return render_template('crear_post.html', user=usuario_verificado)

if __name__ == '__main__':
    app.run(debug=True)
