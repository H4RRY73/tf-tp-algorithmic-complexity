
from grafo import Grafo
from arbol_binario import ArbolBinario
from usuario import Usuario
from post import Post
class GrafoUsuarios:
    def __init__(self):
        self.grafo_usuarios = Grafo()
        self.ufds = {}

    def agregar_usuario(self, correo, usuario):
        self.grafo_usuarios.agregar_nodo(correo, usuario)
        self.ufds[correo] = correo

    def agregar_conexion(self, seguidor, seguido):
        self.grafo_usuarios.agregar_arista(seguidor.correo, seguido.correo)
        seguidor.seguir(seguido)
        self.union(seguidor.correo, seguido.correo)        

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
        recomendaciones=[recomendacion for recomendacion in recomendaciones if recomendacion.correo!=correo and recomendacion not in conexiones_directas]
       
        usuario_verificado = self.buscar_usuario_por_correo(correo)
        

        return recomendaciones

    def _recomendar_conexiones_backtracking(self, conexion, correo, visitados, recomendaciones):
        for siguiente_conexion in self.buscar_conexiones(conexion.correo):
            if siguiente_conexion.correo not in visitados:  # Comprobar el correo en lugar del objeto
                visitados.add(siguiente_conexion.correo)  # Agregar el correo a visitados
                self._recomendar_conexiones_backtracking(siguiente_conexion, correo, visitados, recomendaciones)
                recomendaciones.append(siguiente_conexion)
                if len(recomendaciones) >= 20:  # Limitar el número de recomendaciones
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
    
    def encontrar_representante(self, correo):
        if correo not in self.ufds:
            return None  # El usuario no existe en la UFDS
        path = [correo]
        while self.ufds[path[-1]] != path[-1]:
            path.append(self.ufds[path[-1]])
        for p in path:
            self.ufds[p] = path[-1]  # Compresión de ruta
        return path[-1]

    def union(self, usuario1, usuario2):
        root1 = self.encontrar_representante(usuario1)
        root2 = self.encontrar_representante(usuario2)

        if root1 != root2:
            self.ufds[root1] = root2

    def componentes_conexos(self):
        conjuntos = {}
        for usuario in self.ufds:
            representante = self.encontrar_representante(usuario)
            if representante in conjuntos:
                conjuntos[representante].append(usuario)
            else:
                conjuntos[representante] = [usuario]
        return list(conjuntos.values())
    
class ArbolUsuarios:
     def __init__(self):
        self.arbol_usuarios = ArbolBinario()

    
class RedSocialArbol:
    def __init__(self):
        self.arbol_binario = ArbolBinario()

    def agregar_post(self, autor, contenido):
        post = Post(autor, contenido)
        self.arbol_binario.agregar_objeto(post,post.generar_lista_binaria_intereses())

    

