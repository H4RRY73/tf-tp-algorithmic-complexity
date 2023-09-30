import csv
import json
import random


def generarbinaryList(n):
    a = n * [0]
    for i in range(n):
        a[i] = random.randint(0, 1)
    return a

csv_file = 'Airline Dataset Updated - v2.csv'

datitos = []
max_seguidos = 15

with open(csv_file, mode='r',errors="ignore") as file:
    csv_reader = csv.DictReader(file)
    ID = 0
    for row in csv_reader:

        a = {'ID': ID, 'nombre': row['First Name'], 'apellido': row['Last Name'], 'genero': row['Gender'],
             'edad': row['Age']}
        a['correo'] = a['nombre'] + '_' + a['apellido'] + a['edad'] + '@gmail.com'
        a['contrasena'] = str(random.randint(10 ** 10, 10 ** 12))
        a['interesesBL'] = generarbinaryList(11)
        n_seguidos = random.randint(0, min(ID, max_seguidos)) # limitador para cantidad de seguidos
        lista_seguidos = random.sample(range(ID), n_seguidos) # escoge un aleatorio entre los registros ya creados
        a['seguidosL'] = lista_seguidos
        datitos.append(a)
        ID += 1
    print('se han generado {} registros'.format(ID))

json_file = 'persona.json'


with open(json_file, mode='w') as file:
    json.dump(datitos, file, indent=4)
