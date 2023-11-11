class Usuario:
    def __init__(self, correo, contraseña, nombres, apellidos, edad, genero):
        self.correo = correo
        self.contraseña = contraseña
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.genero = genero
        self.intereses = []

    def agregar_interes(self, interes):
        # Agregar un interés a la lista (si no está duplicado)
        if interes not in self.intereses:
            self.intereses.append(interes)

    def eliminar_interes(self, interes):
        # Eliminar un interés de la lista (si existe)
        if interes in self.intereses:
            self.intereses.remove(interes)
            
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

    def __str__(self):
        return self.correo
