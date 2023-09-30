# usuarios.py
import networkx as nx

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nodo, objeto):
        if nodo not in self.nodos:
            self.nodos[nodo] = {'objeto': objeto, 'vecinos': {}}

    def agregar_arista(self, nodo1, nodo2):
        if nodo1 in self.nodos and nodo2 in self.nodos:
            self.nodos[nodo1]['vecinos'][nodo2] = True
            self.nodos[nodo2]['vecinos'][nodo1] = True

    def obtener_objeto(self, nodo):
        if nodo in self.nodos:
            return self.nodos[nodo]['objeto']
        else:
            return None

    def obtener_vecinos(self, nodo):
        if nodo in self.nodos:
            return list(self.nodos[nodo]['vecinos'].keys())
        else:
            return []


class Usuario:
    def __init__(self, correo, contraseña, nombres, apellidos, edad, genero):
        self.correo = correo
        self.contraseña = contraseña
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.genero = genero

    def __str__(self):
        return self.correo
