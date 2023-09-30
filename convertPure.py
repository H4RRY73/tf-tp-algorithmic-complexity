import csv
import json
import time
import random


def generarbinaryList(n):
    a = n*[0]
    for e in a:
        e = random.randint(0, 1)
    return a

def procesarClavesRapido(datitos, row, rapido, tiempo=0):
    if not rapido:
        print(row)
        time.sleep(tiempo)
    datitos.append(row)


csv_file = 'Airline Dataset Updated - v2.csv'

datitos = []

with open(csv_file, mode='r',errors="ignore") as file:
    csv_reader = csv.DictReader(file)
    cont = 0
    for row in csv_reader:
        a = {'nombre': row['First Name'], 'apellido': row['Last Name'], 'genero': row['Gender'], 'edad': row['Age']}
        a['correo'] = a['nombre'] + '_' + a['apellido'] + a['edad'] + '@gmail.com'
        a['contrasena'] = str(random.randint(10 ** 10, 10 ** 12))
        row['binaryList'] = generarbinaryList(11)
        datitos.append(a)
        cont += 1
    print('se han generado {} registros'.format(cont))

json_file = 'persona.json'


with open(json_file, mode='w') as file:
    json.dump(datitos, file, indent=4)
