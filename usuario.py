class Usuario:
    def __init__(self, correo, contraseña, nombres, apellidos, edad, genero):
        self.correo = correo
        self.contraseña = contraseña
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.genero = genero
        self.intereses = []
        self.lista_binaria_intereses = self.generar_lista_binaria_intereses()
        self.seguidores = []

    def agregar_interes(self, interes):
        # Agregar un interés a la lista (si no está duplicado)
        if interes not in self.intereses:
            self.intereses.append(interes)
            self.lista_binaria_intereses = self.generar_lista_binaria_intereses()

    def eliminar_interes(self, interes):
        # Eliminar un interés de la lista (si existe)
        if interes in self.intereses:
            self.intereses.remove(interes)
            self.lista_binaria_intereses = self.generar_lista_binaria_intereses()

    def generar_lista_binaria_intereses(self):
        # Lista de intereses disponibles en el mismo orden que en la lista binaria
        intereses_disponibles = [
            "Deportes", "Tecnología", "Cine", "Música", "Viajes",
            "Gastronomía", "Arte", "Ciencia", "Moda", "Literatura", "Videojuegos"
        ]

        lista_binaria = []
        for interes_disponible in intereses_disponibles:
            if interes_disponible in self.intereses:
                lista_binaria.append(1)
            else:
                lista_binaria.append(0)

        return tuple(lista_binaria)

    def seguir(self, otro_usuario):
        # Seguir a otro usuario y actualizar las listas de seguidores
        if otro_usuario not in self.seguidores:
            otro_usuario.agregar_seguidor(self)

    def agregar_seguidor(self, seguidor):
        # Agregar un seguidor a la lista (si no está duplicado)
        if seguidor not in self.seguidores:
            self.seguidores.append(seguidor)

    def __str__(self):
        return self.correo
