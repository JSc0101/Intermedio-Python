# Intermedio Python

- en esta seccion vamos aver a python mas a profundidad algunos de sus modules etc...

## Modulos

- aqui podemos observar unno de los modulos mas importante de python

```
* os para operaciones del sistema operativo
* sys para operaciones del intérprete de Python
* math para funciones matemáticas
* random para generación de números aleatorios
* datetime para trabajar con fechas y horas
* json para manejar datos en formato JSON
* urllib para acceder a recursos en línea, como páginas web o API's
* re para trabajar con expresiones regulares
* csv para trabajar con archivos CSV
* pandas para análisis de datos y manipulación de estructuras de datos en tablas
* numpy para operaciones numéricas y matemáticas avanzadas
* matplotlib para visualización de datos
* scikit-learn para aprendizaje automático y minería de datos
* tensorflow o pytorch para aprendizaje profundo (deep learning)
* beautifulsoup4 para analizar y extraer información de páginas web
```

## Datetime

- modulo de fechas

- metodos

```
* datetime.now() devuelve la fecha y hora actual.
* datetime.date() devuelve la fecha actual.
* datetime.time() devuelve la hora actual.
* datetime.datetime.combine() combina una fecha y una hora en un objeto datetime.
* datetime.datetime.strptime() convierte una cadena en un objeto datetime.
* datetime.strftime() convierte un objeto datetime en una cadena con formato * personalizado.
* datetime.timedelta() representa una duración o diferencia entre dos fechas o * tiempos.
* datetime.year devuelve el año de un objeto datetime.
* datetime.month devuelve el mes de un objeto datetime.
* datetime.day devuelve el día de un objeto datetime.
* datetime.hour devuelve la hora de un objeto datetime.
* datetime.minute devuelve el minuto de un objeto datetime.
* datetime.second devuelve el segundo de un objeto datetime.
* datetime.weekday() devuelve el día de la semana como un número entero, donde el lunes es 0 y el domingo es 6.
```

## ejemplos

```
import datetime

# Obtener la fecha y hora actual
ahora = datetime.datetime.now()

# Obtener la fecha actual
hoy = datetime.date.today()

# Obtener la hora actual
hora_actual = datetime.time()

# Combinar una fecha y hora en un objeto datetime
fecha = datetime.date(2023, 2, 19)
hora = datetime.time(10, 30)
fecha_hora = datetime.datetime.combine(fecha, hora)

# Convertir una cadena en un objeto datetime
cadena_fecha = "2023-02-19"
objeto_fecha = datetime.datetime.strptime(cadena_fecha, '%Y-%m-%d')

# Convertir un objeto datetime en una cadena con formato personalizado
cadena_personalizada = ahora.strftime("%Y-%m-%d %H:%M:%S")

# Calcular la diferencia entre dos fechas
fecha1 = datetime.date(2023, 2, 19)
fecha2 = datetime.date(2023, 2, 20)
diferencia = fecha2 - fecha1
print(diferencia.days)  # salida: 1

# Obtener el día de la semana de una fecha
fecha = datetime.date(2023, 2, 19)
dia_semana = fecha.weekday()
print(dia_semana)  # salida: 4 (corresponde al viernes)

```

## list comprehesion

- La comprensión de listas (list comprehension en inglés) es una sintaxis de Python que permite crear listas de una forma más concisa. La sintaxis de la comprensión de listas es la siguiente:

```
[expr for var in lista if cond]

```

- donde expr es una expresión que se evalúa para cada valor de var en lista que cumple la condición cond.

Aquí hay un ejemplo de cómo utilizar la comprensión de listas para crear una lista de los cuadrados de los números del 1 al 5:

```
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados) # salida: [1, 4, 9, 16, 25]

```

## Lambdas

- En Python, una lambda es una función anónima que se utiliza para crear funciones simples en una sola línea de código.

La sintaxis básica de una lambda en Python es la siguiente:

```
lambda x: x**2
```

- Para ver los valores del objeto map que se crea al aplicar una lambda a una lista, puedes convertirlo a una lista o iterar sobre él.

Por ejemplo, si tienes el siguiente código:

```
lista = [1, 2, 3, 4, 5]
resultado = map(lambda x: x**2, lista)

```

## funciones de order superior

- Las funciones de orden superior (también conocidas como funciones de alto nivel o Higher-Order Functions en inglés) son funciones que pueden tomar una o más funciones como argumentos, y/o pueden devolver una función como resultado. En Python, las funciones son objetos de primera clase, lo que significa que se pueden tratar como cualquier otro objeto (por ejemplo, se pueden asignar a variables, se pueden pasar como argumentos a otras funciones, se pueden devolver como resultados de funciones, etc.).

Aquí hay algunos ejemplos de funciones de orden superior en Python:

La función map() toma una función y un iterable como argumentos y aplica la función a cada elemento del iterable, devolviendo un nuevo iterable con los resultados:

```
def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
squares = map(square, numbers)
print(list(squares)) # Output: [1, 4, 9, 16, 25]

```

## Tipos de errores

- En Python, se pueden clasificar los errores en tres tipos: errores de sintaxis (SyntaxError), errores de tiempo de ejecución (RuntimeError) y errores de tiempo de ejecución de excepciones (Exception).

```
# Error de sintaxis: falta el paréntesis de cierre
print("Hola, mundo!"

# Error NameError: la variable 'x' no está definida
print(x)

# Error TypeError: no se puede concatenar un entero y una cadena
x = 5
y = "Hola"
print(x + y)

```

- hay varios errores en python pero estos suelen ser los mas comunes

## ficheros

- En Python, puedes manejar archivos utilizando las funciones y métodos proporcionados por el módulo integrado "os" y "io". Aquí hay un resumen de los pasos comunes para manejar archivos en Python:

```
file = open("archivo.txt", "r")

contenido = file.read()
print(contenido)

file = open("archivo.txt", "w")
file.write("Hola, Mundo!")
file.close()

```

## expresiones regulares

- Las expresiones regulares en Python son una herramienta de procesamiento de cadenas de texto que se utilizan para buscar y manipular patrones de texto en una cadena. Una expresión regular es una secuencia de caracteres que define un patrón de búsqueda y que puede coincidir con una o varias partes de una cadena de texto.

En Python, las expresiones regulares se implementan mediante el módulo "re". Este módulo proporciona funciones que permiten la creación de patrones de expresiones regulares y la realización de operaciones de búsqueda, extracción y reemplazo en cadenas de texto.

Las expresiones regulares en Python se construyen utilizando una sintaxis especial que incluye caracteres especiales y metacaracteres para definir patrones específicos. Por ejemplo, el metacaractero "." se utiliza para representar cualquier carácter, mientras que el metacaractero "^" se utiliza para indicar el inicio de una cadena.

En resumen, las expresiones regulares en Python son una herramienta poderosa para el procesamiento de cadenas de texto y permiten la búsqueda y manipulación de patrones de texto de manera eficiente y flexible.

```
import re

texto = "Hola, ¿cómo estás?"
patron = "estás"

if re.search(patron, texto):
    print("El patrón ha sido encontrado en la cadena de texto")
else:
    print("El patrón no ha sido encontrado en la cadena de texto")


texto = "Mi número de teléfono es 123456789"
patron = r"(\d{9})"

resultado = re.search(patron, texto)

if resultado:
    numero_telefono = resultado.group(1)
    print("El número de teléfono es:", numero_telefono)
else:
    print("No se ha encontrado un número de teléfono en la cadena de texto")

```

## PIP

* PIP es el acrónimo de "Paquete de Instalación de Python" ("Python Package Installer" en inglés), y se refiere a un sistema de gestión de paquetes para Python. PIP permite a los desarrolladores de Python descargar, instalar, actualizar y administrar paquetes y dependencias de software adicionales en sus proyectos de Python de manera sencilla.

* Con PIP, los desarrolladores pueden buscar y descargar fácilmente paquetes de Python de la biblioteca PyPI (Python Package Index), que es un repositorio centralizado de paquetes de software de Python de código abierto. PIP también se puede utilizar para instalar paquetes de Python desde otros repositorios, archivos de distribución o URL.

## instalacion de pip

* La mayoría de las distribuciones modernas de Python incluyen pip como parte de la instalación. Para verificar si pip ya está instalado en su sistema, puede abrir una terminal o línea de comandos y escribir el siguiente comando:

````
pip --version

````

# instalacion window

1. Instalar pip manualmente
Si su sistema operativo no tiene un paquete de gestión de paquetes para instalar pip, puede descargar e instalar pip manualmente. Para hacerlo, siga estos pasos:

Descargue el script de instalación get-pip.py desde el sitio web oficial de pip ejecutando el siguiente comando en una terminal:

````
https://bootstrap.pypa.io/get-pip.py
````

````
python get-pip.py
````

## ehrabuena

* te felicito si has llegado hasta aqui conmigo , ha sido un camino interesante ahora que tienes las bases y conceptos de python necesarios es hora de ponerlos a pruebas en proyectoos y ejercicios , sigue asi tanto como tu y como muchos seguiremos aprendiendo este maravilloso lenguaje

