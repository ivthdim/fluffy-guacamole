# -*- coding: utf-8 -*-
"""Tarea Modulo 1 RESOLUCION.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LnyvKqMwcJwLMOn7b0mHx3ttY0IhKH6c

## Retos:
1. Pregunta al usuario dos números y luego retorna el resultado. Nota: los valores que entran se identifican como string, debes convertirlos a integer o float.
2. Pida al usuario que ingrese tres números. Suma los dos primeros números y luego multiplica este total por el tercero.
3. Escriba un programa que solicite una cantidad de días y luego muestre cuántas horas, minutos y segundos hay en esa cantidad de días.
4. Has un programa que pida al usuario un número mayor a 100 y otro menor 10, y que retorne cuantes veces el número menor cabe dentro del número mayor. Nota: debe retornar un valor entero (integer).
5. Muestra pi (π) con cinco decimales.
6. Explica de manera breve la diferencia entre `math` y `numpy`.
Nota 01: puedes usar el modulo de `numpy` o usar el modulo de `math`.

Nota 02: Recuerda que al introducir un numero usando `input `debes convertirlo a un número float o int.

```python

num = float(input("Introduce un número: ")) # Para el caso de usar float.

```

1-Pregunta al usuario dos números y luego retorna el resultado. Nota: los valores que entran se identifican como string, debes convertirlos a integer o float.
"""

number=int(input('Introduce un numero:'))
number2=int(input('Introduce un numero:'))
print('Los numeros fueron', number, 'y', number2)

"""2-Pida al usuario que ingrese tres números. Suma los dos primeros números y luego multiplica este total por el tercero."""

number=int(input('Introduce un numero:'))
number2=int(input('Introduce un numero:'))
number3=int(input('Introduce un numero:'))

sum=(number+number2)*number3

print(sum)

"""3-Escriba un programa que solicite una cantidad de días y luego muestre cuántas horas, minutos y segundos hay en esa cantidad de días."""

days=int(input('Inserte una cantidad de dias: '))

hours=24*days
minutes=60*hours
seconds=60*minutes

print('El numero de horas en' ,days,'dias es:', hours)
print('El numero de minutos en' ,days,'dias es:', minutes)
print('El numero de minutos en' ,days,'dias es:', seconds)

"""4-Has un programa que pida al usuario un número mayor a 100 y otro menor 10, y que retorne cuantes veces el número menor cabe dentro del número mayor. Nota: debe retornar un valor entero (integer)."""

mayor=int(input('Introduce un número mayor a 100: '))
if mayor <= 100:
  mayor=int(input('El numero que pusiste no es mayor a 100, introduce un número mayor a 100: '))
menor=int(input('Introduce un número menor a 10: '))
if menor >= 10:
  menor=int(input('El numero que pusiste no es menor de 10, introduce un numero menor a 10: '))

caber=int(mayor/menor)

print('El numero',menor, 'cabe',caber, 'veces en' ,mayor)

"""5-Muestra pi (π) con cinco decimales."""

import math

print ("%.5f" % math.pi)

"""6-Explica de manera breve la diferencia entre math y numpy. Nota 01: puedes usar el modulo de numpy o usar el modulo de math.

Math es algo que ya viene en la libreria estandar de python. Tiene algunas constantes relevantes dentro de las matematicas y se usa para algunas operaciones basicas. Por otro lado numpy, es una libreria de terceros, en donde tendremos que se usa por su facilidad para las operaciones vectoriales.

Retos:
1. Pídale al usuario que ingrese su nombre y luego muestre la longitud de su nombre.
2. Pídale al usuario que ingrese su nombre y luego pídale que ingrese su apellido. Únalos con un espacio entre ellos y muestre el nombre y la longitud del nombre completo.
3. Pídale al usuario que escriba cualquier palabra y la muestre en mayúsculas.
4. Pídale al usuario que ingrese su nombre. Si la longitud de su nombre tiene menos de cinco caracteres, pídales que ingresen su apellido y los unan (sin espacios) y muestren el nombre en mayúsculas. Si la longitud del nombre es de cinco o más caracteres, muestre su nombre en minúsculas.
"""

name=input('Ingrese su nombre: ')
longitud=len(name)
print('La longitud de tu nombre es: ',longitud)

"""2-Pídale al usuario que ingrese su nombre y luego pídale que ingrese su apellido. Únalos con un espacio entre ellos y muestre el nombre y la longitud del nombre completo."""

name=input('Ingrese su nombre: ')
last=input('Ingrese su apellido')
lon=len(name+last)
print('Tu nombre es:',name,last, 'y su longitud es:',lon)

"""3-Pídale al usuario que escriba cualquier palabra y la muestre en mayúsculas."""

word=input('Ingresan cualquier palabra: ')
mayus=word.upper()
print(mayus)

"""4-Pídale al usuario que ingrese su nombre. Si la longitud de su nombre tiene menos de cinco caracteres, pídales que ingresen su apellido y los unan (sin espacios) y muestren el nombre en mayúsculas. Si la longitud del nombre es de cinco o más caracteres, muestre su nombre en minúsculas."""

name=input('Ingrese su nombre')
if len(name)<5:
  last=input('Ingrese su apellido')
  mayus=name.upper()
  complete=mayus+last
  print(complete)
else:
  minus=name.lower()
  print(minus)

"""### Tarea/Reto:

1. Pídale al usuario que ingrese su nombre y luego muestre su nombre tres veces.
2. Modifique el programa 1 para que le solicite al usuario que ingrese su nombre y un número y luego muestre su nombre ese número de veces.
3. Pídale al usuario que ingrese su nombre y muestre cada letra de su nombre en una línea separada.
4. Pregunte al usuario en qué dirección quiere contar el usuario (hacia arriba o hacia abajo). Si seleccionan, pídales el número superior y luego cuente desde 1 hasta ese número. Si seleccionan hacia abajo, pídales que ingresen un número inferior a 20 y luego cuenten hacia atrás desde 20 hasta ese número. Si ingresaron algo que no sea arriba o abajo, muestra el mensaje "No entiendo".
5. Pregunte a cuántas personas quiere invitar el usuario a una fiesta. Si ingresan un número inferior a 10, solicite los nombres y después de cada nombre muestre "[nombre] ha sido invitado". Si ingresan un número que es 10 o más, muestra el mensaje "Demasiadas personas".

Nota: En el Reto 4, se tiene que usar el condicional `if`.

1-Pídale al usuario que ingrese su nombre y luego muestre su nombre tres veces.
"""

name=input('Introduce tu nombre: ')
three=3*name
print(three)

"""2-Modifique el programa 1 para que le solicite al usuario que ingrese su nombre y un número y luego muestre su nombre ese número de veces."""

name=input('Introduce tu nombre: ')
veces=int(input('Introduce el numero de veces que quieras que se repita:'))
name_veces=veces*name

print(name_veces)

"""3-Pídale al usuario que ingrese su nombre y muestre cada letra de su nombre en una línea separada."""

name=input('Introduce tu nombre: ')
for letra in name:
  print(letra)

"""4-Pregunte al usuario en qué dirección quiere contar el usuario (hacia arriba o hacia abajo). Si seleccionan, pídales el número superior y luego cuente desde 1 hasta ese número. Si seleccionan hacia abajo, pídales que ingresen un número inferior a 20 y luego cuenten hacia atrás desde 20 hasta ese número. Si ingresaron algo que no sea arriba o abajo, muestra el mensaje "No entiendo"."""

while True:
  entrada=input('Selecciona en que dirección quieres contar:')

  if entrada == 'arriba':
    sup=int(input('Ingresa el numero superior:'))
    for i in range(1,sup+1):
      print(i)
    break
  elif entrada == 'abajo':
    inf=int(input('Ingresa un numero inferior a 20:'))
    if inf < 20:
      for i in reversed(range(1,inf+1)):
        print(i)


    else:
      print('No es menor a 20')
    break
  else:
    print('No te entiendo')

"""5-Pregunte a cuántas personas quiere invitar el usuario a una fiesta. Si ingresan un número inferior a 10, solicite los nombres y después de cada nombre muestre "[nombre] ha sido invitado". Si ingresan un número que es 10 o más, muestra el mensaje "Demasiadas personas"."""

personas=int(input('¿Cuantas personas quieres invitar a tu fiesta? '))

if personas > 10:
  print('Demasiadas personas')
else:
  for i in range(1,personas):
    invitado=input('Nombre del invitado')
    print(invitado, ' ha sido invitado')

"""Retos:
1. Muestra un número entero aleatorio entre 1 y 100 inclusive.
2. Elija aleatoriamente cara o cruz (“h” o “t”). Pídale al usuario que haga su elección. Si su elección es la misma que el valor seleccionado al azar, muestra el mensaje "Tú ganas", de lo contrario muestra "Mala suerte". Al final, dígale al usuario si la computadora seleccionó cara o cruz.
3. Haga una prueba de matemáticas que formule cinco preguntas generando aleatoriamente dos números enteros para formar la pregunta (por ejemplo, [num1] + [num2]). Pídale al usuario que ingrese la respuesta. Si lo hacen bien, suman un punto a su puntuación. Al final del cuestionario, dígales cuántos de cinco acertaron.
4. Muestra cinco colores y pide al usuario que elija uno. Si eligen el mismo que eligió el programa, diga "Bien hecho", de lo contrario muestre una respuesta ingeniosa que involucre el color correcto, por ejemplo. “Apuesto a que estás VERDE de envidia” o “Probablemente te sientas AZUL en este momento”. Pídales que adivinen nuevamente; Si todavía no lo han hecho bien, sigue dándoles la misma pista y pide al usuario que introduzca un color hasta que lo adivine correctamente.

Nota: En el último ejercicio, tendrás que usar el ciclo `while` y el condicional `if`.

1-Muestra un número entero aleatorio entre 1 y 100 inclusive.
"""

import numpy as np

aleatorio = int(np.random.uniform(0, 100))
print(aleatorio)

"""2-Elija aleatoriamente cara o cruz (“h” o “t”). Pídale al usuario que haga su elección. Si su elección es la misma que el valor seleccionado al azar, muestra el mensaje "Tú ganas", de lo contrario muestra "Mala suerte". Al final, dígale al usuario si la computadora seleccionó cara o cruz."""

moneda_u=input('Elija cara (h) o cruz (t): ')

aleatorio_2 = int(np.random.uniform(1, 3))

print(aleatorio_2)

if aleatorio_2 == 1:
  moneda = 'h'
if aleatorio_2 == 2:
  moneda = 't'


if moneda == moneda_u:
    print('Tu ganas')
else:
    print('Mala suerte')


print('Yo elegí:', moneda)

"""3-Haga una prueba de matemáticas que formule cinco preguntas generando aleatoriamente dos números enteros para formar la pregunta (por ejemplo, [num1] + [num2]). Pídale al usuario que ingrese la respuesta. Si lo hacen bien, suman un punto a su puntuación. Al final del cuestionario, dígales cuántos de cinco acertaron."""

puntaje=0
for i in range(1,6):
  alea_1 = int(np.random.uniform(-101, 101))
  alea_2 = int(np.random.uniform(-101, 101))
  answ1=alea_1+alea_2
  print('Haz la suma de los siguientes dos numeros,', alea_1, '+' ,alea_2 )
  ansusu=int(input('Teclea el resultado: '))

  if ansusu == answ1:
    puntaje=puntaje+1


print('Tu puntaje es de:' ,puntaje, 'de 5')

"""4-Muestra cinco colores y pide al usuario que elija uno. Si eligen el mismo que eligió el programa, diga "Bien hecho", de lo contrario muestre una respuesta ingeniosa que involucre el color correcto, por ejemplo. “Apuesto a que estás VERDE de envidia” o “Probablemente te sientas AZUL en este momento”. Pídales que adivinen nuevamente; Si todavía no lo han hecho bien, sigue dándoles la misma pista y pide al usuario que introduzca un color hasta que lo adivine correctamente."""

import numpy as np
alea_1 = int(np.random.uniform(0, 5))

colores=['azul','verde','rojo','amarillo','negro']
print(colores)

maquina=colores[alea_1]
print(maquina)


usuario=input('De la lista de colores ingresa uno: ')

if usuario == maquina:
  print('bien hecho mano')

else:

  while maquina != usuario:


    if maquina == 'azul':
      print('Apuesto a que estas a su lado')

    if maquina == 'verde':
      print('Creo que te puedo ver de lejos')

    if maquina == 'rojo':
      print('Tienes que ver, ojo')

    if maquina == 'amarillo':
      print('Pikachu esta decepcionado')

    if maquina == 'negro':
      print('Cine grotesco')

    usuario=input('De la lista de colores ingresa uno: ')


  print('bien hecho mano')

"""Retos:
1. Defina una función que le pida al usuario que ingrese un número y lo guarde como la variable "num". Luego defina otra función que use "num" y cuente desde 1 hasta ese número. (Nota: sigue la lógia de divide y vencerás).
2. Muestra el siguiente mensaje:
```
1) Sumar
2) Restar
```
Si introduce 1, se generan dos númerso aleatorios antre 5 y 20, y luego pedirle al usuario que realice la suma de esos dos números. Después, comprobar si la suma se realizo de manera correcta, y decirle al usuario su realizo de manera correcta o no la operación.
Si se selecciona 2, entonces se deben generar dos números aleatorios, uno entre 25 y 50 (`num_01`), y el otro en 1 y 25 (`num_02`), después se le pedirá al usuario que reste `num_01` menos `num_02`. De igual manera, decir al usuario si la respuesta fue correcta o no.
3. Cree el siguiente menú:
```
1) Agregar a archivo.
2) Ver los registros.
3) Salir del programa.
```
Si el usuario selecciona 1, permítale agregar a un archivo llamado Salaries.csv que almacenará su nombre y salario. Si seleccionan 2, debería mostrar todos los registros en el archivo Salaries.csv. Si seleccionan 3, debería detener el programa. Si seleccionan una opción incorrecta, deberían ver un mensaje de error. Deberán seguir regresando al menú hasta seleccionar la opción 3.
Nota: En este reto, tienes que usar `while` y el modulo `csv`.

1-Defina una función que le pida al usuario que ingrese un número y lo guarde como la variable "num". Luego defina otra función que use "num" y cuente desde 1 hasta ese número. (Nota: sigue la lógia de divide y vencerás).
"""

def guardar_valor(valor):
    return valor

def usar_variable(valor_guardado):

    for i in range(1, int(valor_guardado)):
        print(i)

valor_guardado = guardar_valor(5)
usar_variable(valor_guardado)

"""2-Muestra el siguiente mensaje:

1) Sumar

2) Restar

Si introduce 1, se generan dos númerso aleatorios antre 5 y 20, y luego pedirle al usuario que realice la suma de esos dos números. Después, comprobar si la suma se realizo de manera correcta, y decirle al usuario su realizo de manera correcta o no la operación. Si se selecciona 2, entonces se deben generar dos números aleatorios, uno entre 25 y 50 (num_01), y el otro en 1 y 25 (num_02), después se le pedirá al usuario que reste num_01 menos num_02. De igual manera, decir al usuario si la respuesta fue correcta o no.
"""

import numpy as np



def option_1():
  alea = int(np.random.uniform(5, 21))
  alea_2 = int(np.random.uniform(5, 21))
  print('Realiza la suma de los siguientes numeros:' ,alea, 'y' ,alea_2)
  suma_usuario=int(input())
  suma_maquina=alea+alea_2


  if suma_usuario == suma_maquina:
    print('Bien hecho mano')

  else:
    while suma_usuario != suma_maquina:
      print('Lo estas haciendo mal')
      suma_usuario=int(input())
    print('Bien hecho mano')



def option_2():
  num_02 = int(np.random.uniform(1, 26))
  num_01 = int(np.random.uniform(25, 51))
  print('Realiza la resta de los siguientes numeros:' ,num_01, 'y' ,num_02)
  resta_usuario=int(input())
  resta_maquina=num_01-num_02


  if resta_usuario == resta_maquina:
    print('Bien hecho mano')

  else:
    while resta_usuario != resta_maquina:
      print('Lo estas haciendo mal')
      resta_usuario=int(input())
    print('Bien hecho mano')





def main_menu():
    print("0. Salir")
    print("1. Sumar")
    print("2. Restar")


    while True:
        choice = input("Elige una opcion entre (0-2): ")

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()

        elif choice == "0":
            print("Aios")
            break
        else:
            print("Entrada Invalida")

if __name__ == "__main__":
    main_menu()

"""3. Cree el siguiente menú:
```
1) Agregar a archivo.
2) Ver los registros.
3) Salir del programa.
```
Si el usuario selecciona 1, permítale agregar a un archivo llamado Salaries.csv que almacenará su nombre y salario. Si seleccionan 2, debería mostrar todos los registros en el archivo Salaries.csv. Si seleccionan 3, debería detener el programa. Si seleccionan una opción incorrecta, deberían ver un mensaje de error. Deberán seguir regresando al menú hasta seleccionar la opción 3.
Nota: En este reto, tienes que usar `while` y el modulo `csv`.
"""

import csv

def option_1():
  nombre = input("Ingrese su nombre: ")
  salario = input("Ingrese su salario: ")

    # Guardar en el archivo Salaries.csv
  with open('salarios.csv', mode='a', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow([nombre, salario])


def option_2():
  with open('salarios.csv', mode='r', newline='') as archivo_csv:
     lector_csv = csv.reader(archivo_csv, delimiter=',')
     for fila in lector_csv:
      print(fila)


def option_3():
    print("Aios")




def main_menu():
    print("Welcome to the Python Menu!")
    print("1. Option 1")
    print("2. Opción 2")
    print("3. Salida")


    while True:
        choice = input("Ingrese una opcion (1-3): ")

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            print("Aios")
            break
        else:
            print("Entrada incorrecta, intenta una vez mas.")

if __name__ == "__main__":
    main_menu()

"""Retos:

1. Crear una clase Persona: Define una clase llamada `Person` que tenga atributos como `name`, `age`, y `city`. Luego, crea objetos de esta clase para representar diferentes personas y accede a sus atributos. Y crea ejemplos donde se solicite la información de una persona creada.
2. Crear una clase Rectangulo: Define una clase llamada `Rectangle` que tenga atributos `height` y `width`. Luego, agrega métodos para calcular el área y el perímetro del rectángulo. Luego crea un ejemplo, donde se crea un rectangulo y se obtiene tanto la informaicón de su área, como de su périmetro.
3. Crear una clase Estudiante: Define una clase llamada `Student` que herede de la clase Persona (`Person`) (del ejercicio 1). Agrega atributos adicionales como grado y promedio academico. Luego, crea objetos de esta clase para representar diferentes estudiantes y accede tanto a los atributos heredados como a los propios.

1-Crear una clase Persona: Define una clase llamada Person que tenga atributos como name, age, y city. Luego, crea objetos de esta clase para representar diferentes personas y accede a sus atributos. Y crea ejemplos donde se solicite la información de una persona creada.
"""

class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def presentacion(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}.")

persona1 = Persona("Alan", 30, 'CDMX')
persona2 = Persona("Benjamin", 25, 'Londres')
persona3 = Persona("Charlie", 35, 'Italia')

print(persona1.nombre)
print(persona1.edad)
print(persona1.ciudad)

print(persona2.nombre)
print(persona2.edad)
print(persona2.ciudad)

print(persona3.nombre)
print(persona3.edad)
print(persona3.ciudad)

persona1.presentacion()

persona2.presentacion()

persona3.presentacion()

"""2-Crear una clase Rectangulo: Define una clase llamada Rectangle que tenga atributos height y width. Luego, agrega métodos para calcular el área y el perímetro del rectángulo. Luego crea un ejemplo, donde se crea un rectangulo y se obtiene tanto la informaicón de su área, como de su périmetro."""

class Rectangulo:
    def __init__(self, altura, ancho):
        self.altura = altura
        self.ancho = ancho

    def area(self):
        return self.altura*self.ancho

    def perimetro(self):
        return 2 * self.altura + 2 * self.ancho

rectangulo = Rectangulo(3,2)

rectangulo.area()

rectangulo.perimetro()

"""3-Crear una clase Estudiante: Define una clase llamada Student que herede de la clase Persona (Person) (del ejercicio 1). Agrega atributos adicionales como grado y promedio academico. Luego, crea objetos de esta clase para representar diferentes estudiantes y accede tanto a los atributos heredados como a los propios."""

class Estudiante(Persona):
    def __init__(self, nombre, edad, ciudad, grado, promedio):
        super().__init__(nombre, edad, ciudad)  # Llamada al constructor de la clase base
        self.grado = grado
        self.promedio = promedio

estudiante1=Estudiante('Carlos',29,'CDMX','Licenciatura',8.4)

print(estudiante1.grado)

print(estudiante1.nombre)

"""Retos:

1-Crear una Serie de precios de productos: Crea una Serie que represente los precios de diferentes productos en una tienda. Utiliza nombres de productos como índices y asigna precios aleatorios. Luego, filtra la Serie para mostrar solo los productos con un precio mayor a cierto valor específico.

2-Crear una Serie de calificaciones de estudiantes: Crea una Serie que represente las calificaciones de diferentes estudiantes en un examen. Utiliza los nombres de los estudiantes como índices y asigna calificaciones aleatorias entre 0 y 100. Luego, calcula el promedio de las calificaciones y muestra las calificaciones de los estudiantes que superaron este promedio.

3-Crear una Serie de temperaturas diarias: Crea una Serie que represente las temperaturas diarias registradas en una ciudad durante una semana. Utiliza los nombres de los días de la semana como índices y asigna temperaturas aleatorias. Luego, calcula la temperatura promedio de la semana y muestra los días donde la temperatura superó este promedio.

1-Crear una Serie de precios de productos: Crea una Serie que represente los precios de diferentes productos en una tienda. Utiliza nombres de productos como índices y asigna precios aleatorios. Luego, filtra la Serie para mostrar solo los productos con un precio mayor a cierto valor específico.
"""

import pandas as pd
import numpy as np

np.random.seed(43)

precios = np.random.randint(1, 100, size=10)
serie_aleatoria = pd.Series(precios)

indices = ['jabon', 'papel', 'pilas', 'chetos','refresco','jugo','leche','huevos','jamon','queso']
serie = pd.Series(precios, index=indices)

print(serie)

filtro = serie[serie > 50]
print(filtro)

"""2-Crear una Serie de calificaciones de estudiantes: Crea una Serie que represente las calificaciones de diferentes estudiantes en un examen. Utiliza los nombres de los estudiantes como índices y asigna calificaciones aleatorias entre 0 y 100. Luego, calcula el promedio de las calificaciones y muestra las calificaciones de los estudiantes que superaron este promedio."""

np.random.seed(7)

calificaciones = np.random.randint(0, 100, size=10)
serie_aleatoria = pd.Series(precios)

indices = ['Carlos', 'Barbara', 'Rosa', 'Julio','Daniela','Eli','Ricardo','Claudia','Alison','Armando']
serie = pd.Series(precios, index=indices)

print(serie)

promedio = serie.mean()
print(promedio)

mayor_promedio=serie[serie > promedio]
print(mayor_promedio)

"""3-Crear una Serie de temperaturas diarias: Crea una Serie que represente las temperaturas diarias registradas en una ciudad durante una semana. Utiliza los nombres de los días de la semana como índices y asigna temperaturas aleatorias. Luego, calcula la temperatura promedio de la semana y muestra los días donde la temperatura superó este promedio."""

import numpy as np
import pandas as pd


np.random.seed(17)


data_aleatoria = np.round(np.random.rand(7) * 100, 2)
serie_aleatoria = pd.Series(data_aleatoria)
indices = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
temperaturas = pd.Series(data_aleatoria, index=indices)

print(temperaturas)

temperatura_promedio=temperaturas.mean()
print(temperatura_promedio)

filtro=temperaturas[temperaturas>temperatura_promedio]
print(filtro)

"""Retos:
1. **Explicación de expresión regular:**
   - Explica con tus palabras que está haciendo la siguiente expresión regular: `[\w\.-]+@[\w\.-]+`.
2. **Validar y retorn la direcciones de correo electrónico**:
   - Cadena de texto: "Ejemplo de dirección de correo electrónico: usuario@example.com"

3. **Extracción de números de teléfono**:
   - Cadena de texto: "Teléfono de contacto: 123-456-7890, Teléfono móvil: (987) 654-3210"

4. **Búsqueda de palabras clave en un texto**:
   - Cadena de texto: "Este es un ejemplo de texto donde queremos buscar la palabra clave 'ejemplo'."

**Explicación de expresión regular:**
   
   1- Explica con tus palabras que está haciendo la siguiente expresión regular: `[\w\.-]+@[\w\.-]+`.

Lo que hace la expresion es buscar cadenas de texto que cumplan con el formato que usualmente tiene una dirección de correo electronico sin tomar en cuenta el dominio superior.

2. **Validar y retorn la direcciones de correo electrónico**:
   - Cadena de texto: "Ejemplo de dirección de correo electrónico: usuario@example.com"
"""

import re

def coincidencias(texto):
  import re
  patron=r'[\w\.-]+@[\w\.-]+\.'
  resultado = re.search(patron, texto)
  if resultado:
    print("Coincidencia encontrada:")
    return resultado.group()
  else:
    print("No se encontró ninguna coincidencia.")

coincidencias("Ejemplo de dirección de correo electrónico: usuario@example.com")

"""3. **Extracción de números de teléfono**:
   - Cadena de texto: "Teléfono de contacto: 123-456-7890, Teléfono móvil: (987) 654-3210"
"""

def telefonos(texto):
  import re
  patron=r'(\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4})'
  resultado = re.findall(patron, texto)
  if resultado:
    print("Coincidencia encontrada:")
    print(resultado)
  else:
    print("No se encontró ninguna coincidencia.")

telefonos("Teléfono de contacto: 123-456-7890, Teléfono móvil: (987) 654-3210")

"""4. **Búsqueda de palabras clave en un texto**:
   - Cadena de texto: "Este es un ejemplo de texto donde queremos buscar la palabra clave 'ejemplo'."
"""

def ejemplo(texto):
  import re
  patron=r'\bejemplo\b'
  resultado = re.findall(patron, texto)
  if resultado:
    print("Coincidencia encontrada:")
    print(resultado)
  else:
    print("No se encontró ninguna coincidencia.")

ejemplo( "Este es un ejemplo de texto donde queremos buscar la palabra clave 'ejemplo'.")

"""Reto:

* Realizar WebScraping, se permite replicar el proyecto de algún tutorial que se encuentre en linea. En caso de replicar un proyecto, se tiene que describir linea a linea que está haciendo.
"""

import requests

standings_url = "https://fbref.com/es/comps/9/2021-2022/Estadisticas-2021-2022-Premier-League"

data =requests.get(standings_url)

data.text #Todos los elementos en HTML de la pagina

from bs4 import BeautifulSoup

soup = BeautifulSoup(data.text)

standings_table=soup.select('table.stats_table')[0] #Hacemos esto para selccionar la primer tabla de estadiscticas dentro de la pagina, ya que esa es la que nos interesa.

standings_table

links = standings_table.find_all('a') #Para encontrar todos los links dentro de la tabla

links

links=[l.get('href') for l in links] #Obtener los links que ya habiamos encontrado

links

links = [l for l in links if '/equipos/' in l] #Para filtrar todos los links que solo esten relacionados con el equipo

links

team_urls = [f'https://fbref.com{l}' for l in links] #Como los links que obtuvimos no tienen la parte inicial del dominio, se lo agregamos

team_urls

"""Ahora nuestro objetivo es extraer cada una de las estadisticas de estos equipos."""

equipo_url= team_urls[0] #Nos enfocamos en el primer equipo que en este caso

data = requests.get(equipo_url)

data.text

import pandas as pd

matches = pd.read_html(data.text, match='Marcadores y partidos ')[0]

matches.head()

print(type(matches))

"""Por ultimo vamos a hacer una iteracion para hacerlo con cada uno de los equipos y vamos a unir los data frame."""

dataframes = []

for i in range(1, 20):
    equipo_url = team_urls[i]

    try:

        response = requests.get(equipo_url)
        response.raise_for_status()  #Se hace la solicitud HTTP, queremos ver si el estatus es 200


        matches = pd.read_html(response.text, match='Marcadores y partidos')[0]
        dataframes.append(matches) #Leemos el dataframe

    except Exception as e:
        print(f"Error al procesar {equipo_url}: {e}") #Si el estatus no es 200, que nos diga en que url hubo un problema

# Concatenar todos los DataFrames
df_final = pd.concat(dataframes, ignore_index=True) #Al final de cualquier manera concatenar los df que sí tengamos.

# Mostrar el DataFrame final
print(df_final)