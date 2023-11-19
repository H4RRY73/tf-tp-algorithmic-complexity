from datetime import datetime

class Post:
    def __init__(self, autor, contenido):
        self.autor = autor
        self.contenido = contenido
        self.fecha_creacion = datetime.now()
        self.intereses = []

    def generar_lista_binaria_intereses(self):
        # Lista de intereses disponibles en el mismo orden que en la lista binaria
        intereses_disponibles = [
            "Deportes", "Tecnología", "Cine", "Música", "Viajes",
            "Gastronomía", "Arte", "Ciencia", "Moda", "Literatura" , "Videojuegos"
        ]

        lista_binaria = []
        for interes_disponible in intereses_disponibles:
            if interes_disponible in self.intereses:
                lista_binaria.append(1)
            else:
                lista_binaria.append(0)

        return tuple(lista_binaria)

   