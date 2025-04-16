# ==============================================================================
# CLASE: Operadores en Python
# ==============================================================================

# Los operadores en Python se utilizan para realizar operaciones sobre variables y valores.

# ----------------------------------------------------
# 42. Operadores Aritméticos
# ----------------------------------------------------
a = 10
b = 3

# Suma
print("Suma:", a + b)

# Resta
print("Resta:", a - b)

# Multiplicación
print("Multiplicación:", a * b)

# División
print("División:", a / b)  # Devuelve un float

# División entera
print("División entera:", a // b)  # Devuelve la parte entera

# Módulo (residuo)
print("Módulo:", a % b)

# Potenciación
print("Potencia:", a ** b)

# ----------------------------------------------------
# 43. Operadores de Asignación
# ----------------------------------------------------
x = 5  # Asignación simple
x += 3  # Suma y asigna (x = x + 3)
x -= 2  # Resta y asigna
x *= 2  # Multiplica y asigna
x /= 3  # Divide y asigna
x %= 4  # Módulo y asigna
x **= 2  # Potencia y asigna
x //= 2  # División entera y asigna

print("Resultado final de x:", x)

# ----------------------------------------------------
# 45. Operadores de Comparación
# ----------------------------------------------------
a = 10
b = 20

print("a == b:", a == b)  # Igualdad
print("a != b:", a != b)  # Diferente
print("a > b:", a > b)    # Mayor que
print("a < b:", a < b)    # Menor que
print("a >= b:", a >= b)  # Mayor o igual
print("a <= b:", a <= b)  # Menor o igual

# ----------------------------------------------------
# 46. Operador Lógico and
# ----------------------------------------------------
usuario_vip = True
compra_mayor_100 = True

if usuario_vip and compra_mayor_100:
    print("Descuento aplicado")

# ----------------------------------------------------
# 47. Ejercicio - Sistema de Descuentos VIP
# ----------------------------------------------------
# Entrada: ¿Es VIP? ¿Compra mayor a 100?
# Salida: Aplicar descuento solo si ambas condiciones son verdaderas.

vip = True
monto_compra = 120

if vip and monto_compra > 100:
    print("Aplica descuento del 20%")
else:
    print("No aplica descuento")

# ----------------------------------------------------
# 48. Operador Lógico or
# ----------------------------------------------------
tiene_carnet = False
es_estudiante = True

if tiene_carnet or es_estudiante:
    print("Puede tomar libros prestados")

# ----------------------------------------------------
# 49. Ejercicio - Préstamo de Libros
# ----------------------------------------------------
# Permitir préstamo si tiene carnet o si es estudiante

carnet = False
estudiante = False

if carnet or estudiante:
    print("Préstamo autorizado")
else:
    print("Acceso denegado")

# ----------------------------------------------------
# 50. Operador Lógico not
# ----------------------------------------------------
activo = False

if not activo:
    print("El usuario está inactivo")

# ----------------------------------------------------
# 51-52. Ejercicio Ticket de Venta (con y sin descuento)
# ----------------------------------------------------
producto = "Teclado"
precio = 100
descuento = 0.1  # 10% de descuento

# Aplicar descuento si precio mayor a 50
if precio > 50:
    precio_final = precio * (1 - descuento)
else:
    precio_final = precio

print("Producto:", producto)
print("Precio final:", precio_final)

# ----------------------------------------------------
# 53-54. Sistema de Autenticación
# ----------------------------------------------------
usuario_esperado = "admin"
clave_esperada = "1234"

usuario_ingresado = "admin"
clave_ingresada = "1234"

if usuario_ingresado == usuario_esperado and clave_ingresada == clave_esperada:
    print("Acceso concedido")
else:
    print("Acceso denegado")

# ----------------------------------------------------
# 55. Precedencia de Operadores
# ----------------------------------------------------
# Paréntesis > Potencia > Multiplicación/División > Suma/Resta
resultado = 3 + 2 * 2  # Resultado = 7
resultado2 = (3 + 2) * 2  # Resultado = 10
print("Resultado 1:", resultado)
print("Resultado 2:", resultado2)

# ----------------------------------------------------
# 56-57. Ejercicio - Valor dentro de Rango
# ----------------------------------------------------
numero = 15
rango_min = 10
rango_max = 20

if numero >= rango_min and numero <= rango_max:
    print("Número dentro de rango")
else:
    print("Número fuera de rango")

# ----------------------------------------------------
# 58-59. Área de un Rectángulo
# ----------------------------------------------------
# Fórmula: área = base * altura
base = 5
altura = 10

area = base * altura
print("Área del rectángulo:", area)
