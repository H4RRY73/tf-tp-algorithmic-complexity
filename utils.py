
from grafo import Grafo
from arbol_binario import ArbolBinario
from usuario import Usuario
class GrafoUsuarios:
    def __init__(self):
        self.grafo_usuarios = Grafo()

    def agregar_usuario(self, correo, usuario):
        self.grafo_usuarios.agregar_nodo(correo, usuario)

    def agregar_conexion(self, correo1, correo2):
        self.grafo_usuarios.agregar_arista(correo1, correo2)

    def buscar_usuario_por_correo(self, correo):
        return self.grafo_usuarios.obtener_objeto(correo)
    
    def buscar_conexiones(self, usuario):        
        conexiones = self.grafo_usuarios.obtener_vecinos(usuario)        
        return conexiones  

    def recomendar_conexiones(self, correo):
        visitados = set()
        conexiones_directas = self.buscar_conexiones(correo)
        recomendaciones = []

        for conexion_directa in conexiones_directas:
            visitados.add(conexion_directa.correo)  # Agregar el correo a visitados
            self._recomendar_conexiones_backtracking(conexion_directa, correo, visitados, recomendaciones)

        # Eliminar conexiones directas y el propio usuario de las recomendaciones
        recomendaciones = [recomendacion for recomendacion in recomendaciones if recomendacion.correo != correo and recomendacion not in conexiones_directas]
        
        return recomendaciones

    def _recomendar_conexiones_backtracking(self, conexion, correo, visitados, recomendaciones):
        for siguiente_conexion in self.buscar_conexiones(conexion.correo):
            if siguiente_conexion.correo not in visitados:  # Comprobar el correo en lugar del objeto
                visitados.add(siguiente_conexion.correo)  # Agregar el correo a visitados
                self._recomendar_conexiones_backtracking(siguiente_conexion, correo, visitados, recomendaciones)
                recomendaciones.append(siguiente_conexion)
                if len(recomendaciones) >= 10:  # Limitar el número de recomendaciones
                    return     
    
    def recomendar_conexiones_con_intereses_similares(self, usuario):
       
        todos_los_usuarios = [u for u in self.grafo_usuarios.nodos.values() if u['objeto'] != usuario]

        # Calcular la similitud de intereses para todos los usuarios
        similitudes = [(otro_usuario['objeto'], self.calcular_similitud_jaccard(usuario, otro_usuario['objeto'])) for otro_usuario in todos_los_usuarios]
       
        # Ordenar los usuarios por similitud en orden descendente
        similitudes.sort(key=lambda x: x[1], reverse=True)

        # Seleccionar las mejores recomendaciones (por ejemplo, los 5 usuarios más similares)
        recomendaciones = [usuario for usuario, similitud in similitudes[:5]]

        return recomendaciones

    def calcular_similitud_jaccard(self, usuario1, usuario2):
        intereses1 = set(usuario1.intereses)
        intereses2 = set(usuario2.intereses)
        interseccion = intereses1.intersection(intereses2)
        union = intereses1.union(intereses2)
        return len(interseccion) / len(union)

class ArbolUsuarios:
     def __init__(self):
        self.arbol_usuarios = ArbolBinario()

    

