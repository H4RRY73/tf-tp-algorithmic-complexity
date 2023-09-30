
from grafo import Grafo

class GrafoUsuarios:
    def __init__(self):
        self.grafo_usuarios = Grafo()

    def agregar_usuario(self, correo, usuario):
        self.grafo_usuarios.agregar_nodo(correo, usuario)

    def agregar_conexion(self, correo1, correo2):
        self.grafo_usuarios.agregar_arista(correo1, correo2)

    def buscar_usuario_por_correo(self, correo):
        return self.grafo_usuarios.obtener_objeto(correo)

    def buscar_conexiones(self, correo):
        usuario = self.buscar_usuario_por_correo(correo)
        if usuario:
            conexiones = self.grafo_usuarios.obtener_vecinos(correo)
            return [self.grafo_usuarios.obtener_objeto(correo) for correo in conexiones]
        return []

