"""
========================================================
Guía Completa para Clase de Python
========================================================
Esta guía abarca desde los temas básicos hasta ejercicios prácticos,
incluyendo:
 15. Variables en Python con ChatGPT
 16. Ejemplo de Variables con Python
 17. Modificación de Variables
 18. Reglas para las Buenas Prácticas con Python y ChatGPT
 19. Ejemplo de Reglas de Buenas Prácticas
 20. Tipos de Datos en Python con ChatGPT
 21. Ejemplo de Tipos de Datos en Python
 22. Ejercicio Propuesto: Datos de un Producto
 23. Solución: Datos de un Producto
 24. Ejercicio Propuesto: Datos de un Vehículo
 25. Solución: Datos de un Vehículo
 26. Cadenas en Python
 27. Caracteres Especiales en Python
 28. Concatenación de Cadenas en Python
 29. Formato de Cadenas en Python
 30. Largo de una Cadena en Python
 31. Métodos Mayúsculas y Minúsculas en Python
 32. Manejo de Subcadenas en Python
 33. Capturar información por Consola en Python
 34. Ejercicio Propuesto - Preséntate con Python (Nueva versión)
 35. Solución Ejercicio - Preséntate con Python (Nueva versión)
 36. Ejercicio Propuesto - Receta de Cocina
 37. Solución Ejercicio - Receta de Cocina
 38. Ejercicio Propuesto - Generador de ID Único
 39. Solución Ejercicio - Generador de ID Único
 40. Ejercicio Propuesto - Generador de Nombres de Emails
 41. Solución Ejercicio - Generador de Nombres de Emails

Cada sección está comentada para facilitar la comprensión y servir de material de consulta.
"""

# ==========================================================================
# 15. Variables en Python con ChatGPT
# ==========================================================================
# En Python una variable es un nombre referencial a un objeto en memoria.
numero = 100                      # Tipo entero (int)
mensaje = "Hola, Python con ChatGPT"  # Tipo cadena (str)

print("15. Variable 'numero':", numero)
print("15. Variable 'mensaje':", mensaje)

# ==========================================================================
# 16. Ejemplo de Variables con Python
# ==========================================================================
# Ejemplo práctico de asignación de variables.
edad = 25                         # Asignación de un entero a "edad"
nombre = "María"                  # Asignación de una cadena a "nombre"
es_estudiante = True              # Variable booleana

# Se imprime cada variable con su descripción.
print("\n16. Ejemplo de Variables:")
print("Edad:", edad)
print("Nombre:", nombre)
print("Es estudiante:", es_estudiante)

# ==========================================================================
# 17. Modificación de Variables
# ==========================================================================
# Una variable puede ser modificada asignándole un nuevo valor, incluso de un tipo distinto.
valor = 10
print("\n17. Valor inicial:", valor)

valor = "Ahora soy una cadena"
print("17. Valor modificado:", valor)

# ==========================================================================
# 18. Reglas para las Buenas Prácticas con Python y ChatGPT
# ==========================================================================
# Buenas prácticas recomendadas (PEP8) incluyen:
# - Nombres descriptivos para variables y funciones.
# - Uso de 'snake_case' para nombres compuestos.
# - Código legible, con comentarios y líneas no muy extensas.
# - Separar la lógica en funciones para facilitar el mantenimiento.

# ==========================================================================
# 19. Ejemplo de Reglas de Buenas Prácticas
# ==========================================================================
def calcular_area_rectangulo(ancho: float, alto: float) -> float:
    """
    Calcula el área de un rectángulo.

    Parámetros:
        ancho (float): Medida horizontal del rectángulo.
        alto (float): Medida vertical del rectángulo.

    Retorna:
        float: El área calculada (ancho * alto).
    """
    return ancho * alto

# Ejemplo de uso
ancho_rect = 5.0
alto_rect = 3.0
area_rect = calcular_area_rectangulo(ancho_rect, alto_rect)
print("\n19. Área del rectángulo:", area_rect)

# ==========================================================================
# 20. Tipos de Datos en Python con ChatGPT
# ==========================================================================
# Python posee distintos tipos de datos básicos:
# - int: Enteros (ej. 42)
# - float: Decimales (ej. 3.14)
# - bool: Booleanos (True/False)
# - str: Cadenas de texto
# Además, estructuras compuestas como list, tuple, dict y set.
# ChatGPT puede proporcionar ejemplos y explicaciones en tiempo real sobre estos.

# ==========================================================================
# 21. Ejemplo de Tipos de Datos en Python
# ==========================================================================
# Ejemplos de distintos tipos de datos:
entero = 42                     # int
flotante = 3.1416               # float
booleano = False                # bool
cadena = "Python es versátil"   # str

lista = [1, 2, 3, 4]            # list (colección ordenada y mutable)
tupla = (5, 6, 7)               # tuple (inmutable)
diccionario = {"clave": "valor", "numero": 10}  # dict (pares clave-valor)
conjunto = {1, 2, 3}            # set (colección de elementos únicos)

print("\n21. Tipos de Datos:")
print("Entero:", entero)
print("Flotante:", flotante)
print("Booleano:", booleano)
print("Cadena:", cadena)
print("Lista:", lista)
print("Tupla:", tupla)
print("Diccionario:", diccionario)
print("Conjunto:", conjunto)

# ==========================================================================
# 22. Ejercicio Propuesto: Datos de un Producto
# ==========================================================================
# Crear una estructura (diccionario) para almacenar:
# - Nombre del producto
# - Precio
# - Stock disponible

# ==========================================================================
# 23. Solución: Datos de un Producto - Solución
# ==========================================================================
def crear_producto(nombre: str, precio: float, stock: int) -> dict:
    """
    Crea un diccionario que representa un producto.

    Parámetros:
        nombre (str): Nombre del producto.
        precio (float): Precio unitario.
        stock (int): Cantidad disponible.

    Retorna:
        dict: Diccionario con los datos del producto.
    """
    producto = {"nombre": nombre, "precio": precio, "stock": stock}
    return producto

# Ejemplo de uso
producto_ej = crear_producto("Laptop", 999.99, 15)
print("\n23. Producto creado:", producto_ej)

# ==========================================================================
# 24. Ejercicio Propuesto: Datos de un Vehículo
# ==========================================================================
# Crear una estructura para almacenar:
# - Marca
# - Modelo
# - Año de fabricación
# - Precio

# ==========================================================================
# 25. Solución: Datos de un Vehículo
# ==========================================================================
def crear_vehiculo(marca: str, modelo: str, anio: int, precio: float) -> dict:
    """
    Crea un diccionario que contiene la información de un vehículo.

    Parámetros:
        marca (str): Marca del vehículo.
        modelo (str): Modelo del vehículo.
        anio (int): Año de fabricación.
        precio (float): Precio del vehículo.

    Retorna:
        dict: Diccionario con los datos del vehículo.
    """
    vehiculo = {"marca": marca, "modelo": modelo, "anio": anio, "precio": precio}
    return vehiculo

# Ejemplo de uso
vehiculo_ej = crear_vehiculo("Toyota", "Corolla", 2020, 20000.00)
print("\n25. Vehículo creado:", vehiculo_ej)

# ==========================================================================
# 26. Cadenas en Python
# ==========================================================================
# Las cadenas (str) son secuencias inmutables de caracteres.
cadena_ej = "Esta es una cadena de ejemplo."
print("\n26. Cadena:", cadena_ej)

# ==========================================================================
# 27. Caracteres Especiales en Python
# ==========================================================================
# Para representar caracteres especiales se usan secuencias de escape.
texto_escapes = "Línea 1\nLínea 2\tcon tabulación y una barra invertida: \\"
print("\n27. Texto con caracteres especiales:")
print(texto_escapes)

# ==========================================================================
# 28. Concatenación de Cadenas en Python
# ==========================================================================
# Se usa el operador '+' para concatenar.
saludo1 = "Hola"
saludo2 = "Mundo"
saludo_completo = saludo1 + " " + saludo2
print("\n28. Saludo concatenado:", saludo_completo)

# ==========================================================================
# 29. Formato de Cadenas en Python
# ==========================================================================
# Se pueden formatear cadenas de varias maneras:
# 1. Usando el método format()
formateo1 = "El valor es: {}".format(123)
# 2. Usando f-strings (requiere Python 3.6+)
valor_variable = 456
formateo2 = f"El valor variable es: {valor_variable}"
print("\n29. Formateo de cadenas:")
print(formateo1)
print(formateo2)

# ==========================================================================
# 30. Largo de una Cadena en Python
# ==========================================================================
# Se utiliza la función len() para obtener el número de caracteres.
largo_cadena = len(cadena_ej)
print("\n30. Largo de la cadena:", largo_cadena)

# ==========================================================================
# 31. Métodos Mayúsculas y Minúsculas en Python
# ==========================================================================
# upper() y lower() convierten la cadena a mayúsculas o minúsculas, respectivamente.
mayusculas = cadena_ej.upper()
minusculas = cadena_ej.lower()
print("\n31. Cadena en mayúsculas:", mayusculas)
print("31. Cadena en minúsculas:", minusculas)

# ==========================================================================
# 32. Manejo de Subcadenas en Python
# ==========================================================================
# Se utiliza slicing para extraer una parte de la cadena.
# Sintaxis: cadena[inicio:fin] (fin no se incluye)
subcadena = cadena_ej[8:18]
print("\n32. Subcadena extraída:", subcadena)

# ==========================================================================
# 33. Capturar información por Consola en Python
# ==========================================================================
# input() permite leer información introducida por el usuario.
nombre_usuario = input("\n33. Ingresa tu nombre: ")
print("33. ¡Bienvenido,", nombre_usuario + "!")
# Nota: Al usar input(), el valor capturado es de tipo cadena (str).

# ==========================================================================
# 34. Ejercicio Propuesto - Preséntate con Python (Nueva versión)
# ==========================================================================
# Se solicita que el usuario ingrese información personal (nombre, edad, ciudad)
# y se presente en un formato estructurado.

# ==========================================================================
# 35. Solución Ejercicio - Preséntate con Python (Nueva versión)
# ==========================================================================
def presentate():
    """
    Captura datos personales del usuario y muestra una presentación formateada.

    Se solicitan:
        - Nombre (str)
        - Edad (int)
        - Ciudad (str)

    No retorna valor, solo imprime la presentación.
    """
    nombre = input("34. Ingresa tu nombre: ")
    # Convertir la edad a entero después de capturarla como cadena.
    edad = int(input("34. Ingresa tu edad: "))
    ciudad = input("34. Ingresa tu ciudad: ")

    # Formateo de la presentación.
    presentacion = f"¡Hola, mi nombre es {nombre}, tengo {edad} años y soy de {ciudad}."
    print("35. Presentación:\n", presentacion)

# Llamada a la función de presentación (se puede comentar para pruebas automáticas)
# presentate()

# ==========================================================================
# 36. Ejercicio Propuesto - Receta de Cocina
# ==========================================================================
# Se pide capturar datos de una receta:
# - Nombre del plato.
# - Lista de ingredientes (separados por comas).
# - Instrucciones de preparación.
#
# Luego, mostrar la receta de manera formateada.

# ==========================================================================
# 37. Solución Ejercicio - Receta de Cocina
# ==========================================================================
def crear_receta():
    """
    Captura los datos de una receta y retorna un diccionario con la información.

    Se solicitan:
        - Nombre del plato (str)
        - Ingredientes (str): Se espera una cadena separada por comas.
        - Instrucciones (str)

    Retorna:
        dict: Información de la receta.
    """
    nombre_plato = input("36. Nombre del plato: ")
    ingredientes = input("36. Ingresa los ingredientes separados por comas: ")
    instrucciones = input("36. Instrucciones de preparación: ")

    # Separamos los ingredientes en una lista usando split() y eliminamos espacios sobrantes.
    lista_ingredientes = [ingrediente.strip() for ingrediente in ingredientes.split(',')]

    receta = {
        "nombre": nombre_plato,
        "ingredientes": lista_ingredientes,
        "instrucciones": instrucciones
    }
