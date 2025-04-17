# ************ Colecciones en Python ************

# 1. Listas en Python
print('*** Manejo de Listas ***')

# Definición de una lista
mi_lista = [1, 2, 3, 4, 5]
# Accedemos a un elemento por índice
print(f'Accedemos al valor del índice 4: {mi_lista[4]}')  # Salida: 5
print(f'Accedemos al último índice de la lista: {mi_lista[-1]}')  # Salida: 5

# Modificamos el elemento de la lista
mi_lista[1] = 10
print(f'Modificamos el valor del índice 1: {mi_lista[1]}')  # Salida: 10

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)
print(f'Lista después de agregar 6: {mi_lista}')  # Salida: [1, 10, 3, 4, 5, 6]

# Añadimos un elemento en un índice específico
mi_lista.insert(2, 10)
print(f'Lista después de insertar 10 en el índice 2: {mi_lista}')  # Salida: [1, 10, 10, 3, 4, 5, 6]

# Eliminar elementos de la lista
mi_lista.remove(5)  # Remueve el primer elemento con el valor 5
print(f'Lista después de remover 5: {mi_lista}')  # Salida: [1, 10, 10, 3, 4, 6]

mi_lista.pop(1)  # Elimina el elemento con el índice 1
print(f'Lista después de eliminar el índice 1: {mi_lista}')  # Salida: [1, 10, 3, 4, 6]

del mi_lista[2]  # Eliminar usando la palabra "del"
print(f'Lista después de eliminar el índice 2: {mi_lista}')  # Salida: [1, 10, 4, 6]

# Longitud de la lista
print(f'Largo de la lista: {len(mi_lista)}')  # Salida: 4

# Obtener una sublista
sublista = mi_lista[1:3]  # Obtener elementos del índice 1 al 2 (no incluye el 3)
print(f'Sublista: {sublista}')  # Salida: [10, 4]

# 2. Iterar una Lista en Python
print('*** Iterar una Lista ***')
nombres = ['Karla', 'Juan', 'Laura']
for nombre in nombres:
    print(nombre)  # Imprime cada nombre en la lista

# Lista heterogénea
lista_heterogenea = [100, True, 'Ivonne']
for elemento in lista_heterogenea:
    print(elemento)  # Imprime cada elemento en la lista heterogénea

# 3. Ejercicio de un Playlist en Python
print('*** Playlist ***')
# Se define la lista
lista_reproduccion = []
numero_canciones = int(input('Cuántas canciones deseas agregar: '))  # Usuario decide cuántas canciones agregar
for indice in range(numero_canciones):
    cancion = input(f'Proporciona la canción {indice + 1}: ')
    lista_reproduccion.append(cancion)  # Agregar canción a la lista

# Ordenar la lista en orden alfabético en orden ascendente
lista_reproduccion.sort()
print(f'\nLista de Reproducción en orden Alfabético: ')
for cancion in lista_reproduccion:
    print(f'- {cancion}')  # Muestra cada canción en la lista

# 4. Ejercicio Propuesto - Promedio de Calificaciones en Python
print('*** Promedio de Calificaciones ***')
total_calificaciones = int(input('Proporciona el número de calificaciones a evaluar: '))
calificaciones = []  # Crear lista de calificaciones
for indice in range(total_calificaciones):
    calificacion = int(input(f'Calificación[{indice}] = '))  # Sumar calificaciones por usuario
    calificaciones.append(calificacion)  # Agregamos la calificación a la lista
print(f'Las calificaciones proporcionadas son: {calificaciones}')
suma_calificaciones = sum(calificaciones)  # Sumar todas las calificaciones
promedio = suma_calificaciones / total_calificaciones  # Calcular el promedio
print(f'Promedio de las Calificaciones: {promedio}')

# 5. Tuplas en Python
print('*** Manejo de Tuplas ***')
mi_tupla = (1, 2, 3, 4, 5)
print(f'Elemento de la tupla: {mi_tupla}')  # Tupla original
for elemento in mi_tupla:
    print(elemento)  # Iterar sobre los elementos

coordenadas = (3, 5)  # Ejemplo de tupla de coordenadas
print(f'Coordenada x: {coordenadas[0]}, Coordenada y: {coordenadas[1]}')  # Acceder a elementos de coordenadas

# 6. Desempaquetamiento (unpacking) de tuplas en Python
print('*** Desempaquetado de Tuplas ***')
producto = ('P001', 'Camisa', 20.00)  # Tupla de producto
id, descripcion, precio = producto  # Desempaquetamos la tupla
print(f'Id: {id}, Descripción: {descripcion}, Precio: {precio}')  # Muestra los valores desempaquetados

# 7. Combinación de Listas y Tuplas en Python
print('*** Combinación de Listas y Tuplas ***')
productos = [('P001', 'Camiseta', 20.00), ('P002', 'Jeans', 30.00), ('P003', 'Sudadera', 40.00)]
precio_total = 0
print('Información de los productos: ')
for producto in productos:
    id, descripcion, precio = producto  # Unpacking
    print(f'Producto: id = {id}, descripcion = {descripcion}, precio = {precio}')
    precio_total += precio  # Acumular total de precios
print(f'Precio total de los productos: {precio_total}')

# 8. Sets (conjuntos) en Python
print('*** Manejo de Sets ***')
mi_set = {1, 2, 3, 4, 5, 4}  # Crear un conjunto (el 4 duplicado es ignorado)
print(f'Mi set: {mi_set}')  # Imprime conjunto sin duplicados
mi_set.add(6)  # Agregar elemento al conjunto
mi_set.add(7)
mi_set.add(3)  # Intentar agregar elemento duplicado
mi_set.remove(4)  # Eliminar un elemento del conjunto
print(f'Mi set después de eliminar 4: {mi_set}')
print(f'¿El 4 está en el set?: {4 in mi_set}')  # Comprobar existencia de un elemento
print(f'Cantidad total de elementos en mi set: {len(mi_set)}')  # Longitud del conjunto

# 9. Ejercicio Boletín Informativo en Python
print('*** Boletín Informativo ***')
suscriptores = set()  # Definimos el set inicial vacío
numero_suscriptores = int(input('Proporciona el número de suscriptores iniciales: '))
for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))  # Agregar suscriptores
print(f'Lista de suscriptores inicial: {suscriptores}')

nuevo_suscriptor = input('Proporciona el nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya está en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado a la lista {nuevo_suscriptor}')

suscriptor_eliminar = input('Proporciona el suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)  # Eliminar un suscriptor existente
print(f'Lista de suscriptores: {suscriptores}')
print(f'Cantidad total suscriptores: {len(suscriptores)}')

# 10. Diccionarios en Python
print('*** Diccionarios en Python ***')
persona = {
    'nombre': 'Sergio',
    'edad': 30,
    'ciudad': 'México'
}  # Crear un diccionario
print(f'Diccionario de persona: {persona}')
print(f'Nombre: {persona["nombre"]}, Edad: {persona["edad"]}, Ciudad: {persona["ciudad"]}')  # Acceder a los elementos

# Modificar un valor del diccionario
persona['edad'] = 35
persona['profesion'] = 'Ingeniero'  # Agregar un nuevo elemento
print(f'Diccionario actualizado: {persona}')

# Eliminar un elemento
del persona['ciudad']
print(f'Diccionario después de eliminar "ciudad": {persona}')

# Iterar sobre un diccionario
for clave, valor in persona.items():
    print(f'Clave: {clave}, Valor: {valor}')

# 11. Ejercicio Agenda de Contactos - parte 1
print('*** Agenda de Contactos - parte 1 ***')
agenda = {
    "Carlos": { "telefono": "55667711", "email": "carlos@mail.com", "direccion": "Calle Principal 132" },
    "María": { "telefono": "99887733", "email": "maria@mail.com", "direccion": "Avenida Central 456" },
    "Pedro": { "telefono": '55139078', 'email': 'pedro@mail.com', 'direccion': 'Plaza Mayor 789' }
}  # Definimos un diccionario de contactos
print(agenda)

# Acceder a información de un contacto específico
print(f'Información de contacto de María: Teléfono: {agenda["María"]["telefono"]}, Email: {agenda["María"]["email"]}, Dirección: {agenda["María"]["direccion"]}')

# Agregar un nuevo contacto
agenda['Ana'] = { 'telefono': '55678392', 'email': 'ana@mail.com', 'direccion': 'Calle Salvador Diaz 321' }
print(f'Diccionario de agenda después de agregar a Ana: {agenda}')

# Eliminar un contacto existente
agenda.pop('Pedro')  # Eliminar usando el método pop
print(f'Agenda después de eliminar a Pedro: {agenda}')

# Mostrar todos los contactos
print('\nLista de contactos en la agenda:')
for nombre, detalles in agenda.items():
    print(f'Nombre: {nombre}, Teléfono: {detalles["telefono"]}, Email: {detalles["email"]}, Dirección: {detalles["direccion"]}')

# 12. Ejercicio Propuesto - Sistema de Inventarios en Python
print('*** Sistema de Inventarios ***')
inventario = []  # Definimos la variable de inventario
numero_productos = int(input('Cuántos productos deseas agregar al inventario? '))
for indice in range(numero_productos):
    print(f'Proporciona los valores del producto {indice + 1}:')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    # Crear diccionario con el detalle del producto
    producto = {'id': indice, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    inventario.append(producto)  # Agregamos el nuevo producto al inventario
print(f'\nInventario actual: {inventario}')

# Buscar un producto por ID
id_buscar = int(input('\nIngresa el ID del producto a buscar: '))
producto_encontrado = None
for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break
if producto_encontrado:
    print(f'Información del producto encontrado: Id: {producto_encontrado.get("id")}, Nombre: {producto_encontrado.get("nombre")}, Precio: {producto_encontrado.get("precio")}, Cantidad: {producto_encontrado.get("cantidad")}')
else:
    print(f'Producto con id {id_buscar} no encontrado!')

# Mostrar el inventario detallado actualizado
print(f'\nInventario Detallado Actualizado:')
for producto in inventario:
    print(f'Id: {producto.get("id")}, Nombre: {producto.get("nombre")}, Precio: {producto.get("precio")}, Cantidad: {producto.get("cantidad")}')

