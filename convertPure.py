import csv
import json
import random

intereses = ["Deportes", "Tecnologia", "Cine", "Musica", "Viajes", "Gastronomia", "Arte", "Ciencia", "Moda", "Literatura","Videojuegos"]



csv_file = 'Airline Dataset Updated - v2.csv'

datitos = []
max_seguidos = 5
max_seguidores = 5

def generar_intereses():
    n = random.randint(1, len(intereses))
    if random.randint(0, 2) % 2 == 0:
        n = random.randint(3, 4)
    intereses_seleccionados = random.sample(intereses, n)

    return intereses_seleccionados

with open(csv_file, mode='r',errors="ignore") as file:
    csv_reader = csv.DictReader(file)
    ID = 0
    for row in csv_reader:

        a = {'ID': ID, 'nombre': row['First Name'], 'apellido': row['Last Name'], 'genero': row['Gender'],
             'edad': row['Age']}
        a['correo'] = a['nombre'] + '_' + a['apellido'] + a['edad'] + '@gmail.com'
        a['contrasena'] = str(random.randint(10 ** 10, 10 ** 12))
        a['intereses'] = generar_intereses()
        n_seguidos = random.randint(0, min(ID, max_seguidos)) # limitador para cantidad de seguidos
        lista_seguidos = random.sample(range(ID), n_seguidos) # escoge un aleatorio entre los registros ya creados
        a['seguidosL'] = lista_seguidos
        n_seguidos = random.randint (0, min (ID, max_seguidos))
        a['seguidoresL'] = random.sample(range(ID),n_seguidos)
        datitos.append(a)
        ID += 1
    print('se han generado {} registros'.format(ID))

json_file = 'persona.json'


with open(json_file, mode='w') as file:
    json.dump(datitos, file, indent=4)
