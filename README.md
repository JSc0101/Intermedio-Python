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

* modulo de fechas

* metodos
````
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
````

## ejemplos

````
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

````