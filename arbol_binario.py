from usuario import Usuario


class Nodo:
    def __init__(self):
        self.objetos = []
        self.hijo_izquierdo = None
        self.hijo_derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = Nodo()

    def agregar_objeto(self, objeto, lista_binaria):
        nodo_actual = self.raiz

        for bit in lista_binaria:
            if bit == 0:
                if nodo_actual.hijo_derecho is None:
                    nodo_actual.hijo_derecho = Nodo()
                nodo_actual = nodo_actual.hijo_derecho
            else:
                if nodo_actual.hijo_izquierdo is None:
                    nodo_actual.hijo_izquierdo = Nodo()
                nodo_actual = nodo_actual.hijo_izquierdo

        nodo_actual.objetos.append(objeto)

    def buscar_objetos_por_lista_binaria(self, lista_binaria):
        def buscar_nodos(nodo_actual, indice):
            if nodo_actual is None:
                return []

            objetos_coincidentes = []

            if indice == len(lista_binaria):
                # Llegamos al final de la lista binaria, incluir todos los objetos del nodo actual
                objetos_coincidentes.extend(nodo_actual.objetos)
            else:
                bit = lista_binaria[indice]
                if bit == 1:
                    objetos_coincidentes.extend(buscar_nodos(nodo_actual.hijo_izquierdo, indice + 1))
                objetos_coincidentes.extend(buscar_nodos(nodo_actual.hijo_derecho, indice + 1))

            return objetos_coincidentes

        return buscar_nodos(self.raiz, 0)