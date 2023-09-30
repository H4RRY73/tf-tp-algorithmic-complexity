# usuarios.py
import networkx as nx
from usuario import Usuario

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
            return [self.nodos[vecino]['objeto'] for vecino in self.nodos[nodo]['vecinos']]
        else:                     
            return []


