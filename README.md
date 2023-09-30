<br />
<div align="center">
  <a href="https://github.com/H4RRY73/tf-algorithmic-complexity">
    <img src="./logo_transparent.png" width="200px">
  </a>

  <h1 align="center">THE SOCIAL DILEMA</h1>

  <p align="center">
    Peruvian University of Applied Sciences.
    <br />
    Algorithmic Complexity.
    <br />
    Teacher: Luis Martin Canaval Sanchez
  </p>
</div>

**_Integrantes_**
| Apellidos y Nombres | Codigo |
| ------------- | ------------- |
| Cervantes Erequita  | U202110140  |
| Mayta Lopez Harold Jaime | U202114851  |
| Vilchez Marin Rody Sebastian | U202112321 |

## Descripcion del problema
### Contextualizacion
---
> Cuando realizas una búsqueda en Google como 'el cambio climático es...', obtendrás resultados diversos, dependiendo de tu ubicación y de la información que Google tenga sobre tus intereses.
- Netflix, 2020.

Este es el punto de partida de **The Social Dilemma**, un documental que investiga los efectos y peligros vinculados al uso de diversos servicios en línea. En este documental, se pone de relieve cómo los algoritmos utilizados pueden tener un impacto significativo en la política global, como se evidenció durante la *Primavera Árabe*. No obstante, no debemos menospreciar el impacto y la influencia personal que estos algoritmos ejercen sobre los usuarios.

No es sorprendente que ***Stuart Russell***(**2021**), profesor de Inteligencia Artificial en la Universidad de California en Berkeley, expresara en una entrevista con la BBC: *El objetivo principal de estos algoritmos es mejorar la experiencia del usuario en las redes sociales, logrando recopilar la máxima cantidad de información sobre cada usuario y proporcionándoles contenido que se adapte a sus preferencias para mantenerlos conectados por más tiempo*.

### Descripcion del problema
De manera lógica, podemos inferir que el uso de servicios que emplean algoritmos como los mencionados por Russell no guía a los usuarios hacia una mejora constante, sino que los sumerge en un proceso en el que cada vez destinan más tiempo a consumir contenido, en una dinámica poco saludable.

Como grupo, en relacion a esta situacion,  consideramos que las herramientas no poseen una categoría moral en si mismas, y los juicios de este tipo aplican exclusivamente al uso que se les da.  Por lo tanto, creemos que una red social equipada con algoritmos adecuados para orientar a los usuarios hacia un proceso de mejora continua podría ser una valiosa herramienta para aquellos interesados en mantener una buena higiene digital en su consumo de contenidos.

En este sentido, nustro objetivo frente a este problema es crear una una solucion computacional que reconcilie frente al usuario *lo que es* y *lo que quiere ser*.

## Descripción del conjunto de datos **dataset**
[TwitterFriends](https://www.kaggle.com/datasets/hwassner/TwitterFriends)

En cuanto a los criterios de selección del conjunto de datos **dataset**, necesitamos que este cumpla con los siguientes requisitos:

* Lista de Amigos: El dataset debe contener algun tipo de información que realcione 2 usuarios.

* Criterios Parametrizables:  Seria bastante beneficioso **para el cumplimiento de los objetivos** que el dataset incluya criterios parametrizables.

* Mas de 1500 registros: El dataset debe contar con al menos 1500, para asegurar que haya suficientes nodos para simular cierta carga.

Tras una breve busqueda en Kaggle encontramos el dataset [Twitter Friends](https://www.kaggle.com/datasets/hwassner/TwitterFriends). Este dataset cuenta con:

* ID de usuario: Identificador unico para cada usuario. Fungira como identificador de los nodos.

* Lista de Amigos: Almacenados en forma de ID de usuario. Servira para realacionar los nodos.

* Tiempo desde el ultimo Tweet: Parametrizable tras procesar como actividad del usuario.

* Seguidores: Parametrizable a socializacion. Grado interno del user.

* Seguidos: Parametrizable a socializacion. Grado externo del user.

Como ultimas ventajas a mencionar, por un lado es la cantidad de registros, contando con 40 000 registros. Por otro lado, la escalabilidad de este dataset al poder ser reemplazado en entregas posteriores por la API de twitter.

Finalmente, reconocer a ***Hubert Wassner*** (**2016**) creador de este dataset mediante la utilizacion de la API pública de Twitter.

## Propuesta
Una red social con dos posibilidades de carga de contenido. Primero, carga de contenido de acuerdo a comportamientos del usuario. Segundo, carga de contenido de acuerdo a metas del usuario. 

### Objetivo General
* Nuestro objetivo general es crear una red social que, a través del contenido mostrado y las interacciones realizadas, permita guiar al usuario desde su situación actual hacia la consecución de sus metas y aspiraciones, 

### Objetivos Especificos
* Implementar una aplicacion que permita mostrar contenido afin al comportamiento actual del usuario.

* Implementar en la aplicacion un ajuste que permita mostrar contenido afin a los objetivos expresados por el usuario.

### Metodologia 
---
> El pensamiento Lean ... tiene como objetivo garantizar el incremento del valor de un producto/servicio reduciendo el desperdicio en el proceso de creación de este, mejorando la calidad.
- Villanueva y Vizarreta, 2022, p60.


La metodologia a emplear en este trabajo sera LEAN UX, dada la intensidad, e iteracion propuestas para el desarrollo de este proyecto. Asimismo, consideramos que el enfoque solucionador de esta metodologia sera frecuentemente util.

### Tecnicas
* ***Segun describe Flores*** (**2022**), la metodologia Lean UX sugiere que trabajar para alcanzar un MVP (producto minimo viable) e iterar con sprints sobre el.

* Segun las recomendaciones realizadas por ***Canaval** (**comunicación personal, 15 de agosto de 2023**) usaremos el analisis de tiempos Para poder predecir o validar, comportamientos del programa conforme la cantidad de usuarios crezca. La prediccion se realizara con el metodo formal de conteo y la validacion con el metodo de cronometrado. 

### Bibliografias 

1. Netflix. (2020) *The social Dilema* (Youtube) [Link](https://www.youtube.com/watch?v=uaaC57tcci0)

1. Russell, S.(2021) *Por qué los algoritmos de las redes sociales son cada vez más peligrosos.* BBC News Mundo [Link](https://www.bbc.com/mundo/noticias-58874170 )

1. Wassner, H.(2016) *TwitterFriends.* [Link](https://www.kaggle.com/datasets/hwassner/TwitterFriends )

1. Villanueva, F. Vizarreta, R.(2022) *Plataforma Web para la Gestión y Despliegue del Contenido Digital del Grupo de Investigación de Métodos Computacionales Aplicado a Nanomateriales de la UNMSM Desarrollado Bajo el Marco Dual-Track Agile.* (tesis de licenciatur, **Universidad de Piura**) [Repositorio Institucional UDEP.](https://pirhua.udep.edu.pe/handle/11042/5619)

1. Condor, J. (2022). *Metodología para integrar la Experiencia de Usuario en el desarrollo de sistemas web de una entidad pública.* (tesis de licenciatura, **Universidad Cesar Vallejo**). [Repositorio Institucional de la UCV.](https://repositorio.ucv.edu.pe/bitstream/handle/20.500.12692/85437/Condor_FJG-SD.pdf?sequence=1&isAllowed=y)

1. Canaval, L. (2023). Sesión de clase - recording_2 - 15/08/2023 10:53:17 (**Blackboard**). [Blackboard](https://upc-download.obs.la-south-2.myhuaweicloud.com/2023/CC184-2302-WX73/08/20230815_288f6dde5b2a45b1ac81d8dd56a29dd0.mp4?AWSAccessKeyId=GYZ95IQQPU27KYGYXLZD&Expires=1724451425&Signature=9IlUlDYJG%2BiUNV%2FxVmlfLTKvWq4%3D)
