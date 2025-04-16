"""
============================================================
Guía de Estudio - Sentencias de Decisión y Ejercicios en Python
============================================================

Temas incluidos en esta guía:
 60. Sentencias de Decisión en Python
 61. Sentencia if else en Python
 62. Sentencia if elif else en Python
 63. Ejercicio: Valor Positivo en Python
 64. Ejercicio Propuesto - Sistema de Descuentos de una Tienda en Línea
 65. Solución - Sistema de Descuentos de una Tienda en Línea
 66. Ejercicio: Sistema Bancario en Python
 67. Ejercicio Propuesto - El Mayor de dos números en Python
 68. Solución - El Mayor de dos números en Python
 69. Operador Ternario en Python
 70. Ejercicio Propuesto - Estación del Año en Python
 71. Solución - Estación del Año en Python
 72. Ejercicio Propuesto - Mayor de Edad en Python
 73. Solución - Mayor de Edad en Python
 74. Ejercicio Propuesto - Sistema de Calificaciones en Python
 75. Solución - Sistema de Calificaciones en Python
 76. Ejercicio Propuesto - Sistema de Envíos en Python
 77. Solución - Sistema de Envíos en Python
 78. Ejercicio Propuesto - Sistema de Autenticación en Python
 79. Solución - Sistema de Autenticación en Python

Cada sección contiene comentarios que explican el uso de módulos, funciones, atributos y parámetros, para que sirva como una completa guía de estudio.
"""

# =============================================================================
# 60. Sentencias de Decisión en Python
# =============================================================================
# Las sentencias de decisión permiten elegir qué bloque de código ejecutar según condiciones.
# En Python se utilizan "if", "elif" (else if) y "else".
# El concepto clave es evaluar expresiones booleanas (True o False).

# Ejemplo sencillo:
numero = 10
if numero > 5:
    print("El número es mayor que 5")
# En este ejemplo, si la condición "numero > 5" es verdadera, se ejecuta el bloque indentado.

# Ejemplo analizando True/False:

print('*** Sentencias Decisión ***')

dia_con_lluvia = False

if dia_con_lluvia:
    print('Llevar paraguas')
else:
    print('Dejar paraguas en casa')

# =============================================================================
# 61. Sentencia if else en Python
# =============================================================================
# La estructura "if else" permite ejecutar un bloque si la condición es True y otro si es False.
# Sintaxis:
# if condición:
#     # Bloque A
# else:
#     # Bloque B

edad = 20

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
# En este ejemplo, la condición se evalúa y se imprime el mensaje correspondiente.

# =============================================================================
# 62. Sentencia if elif else en Python
# =============================================================================
# Cuando se tienen múltiples condiciones se utiliza "elif".
# Sintaxis:
# if condición1:
#     # Bloque A
# elif condición2:
#     # Bloque B
# else:
#     # Bloque C

nota = 75

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bueno")
else:
    print("Necesita mejorar")
# Se evalúa la primera condición, y si es False se pasa a la siguiente.

# =============================================================================
# 63. Ejercicio - Valor Positivo en Python
# =============================================================================
# Ejercicio: Pedir al usuario que ingrese un número y determinar si es positivo.

# Ejemplo con comentarios:
numero_input = float(input("Ingrese un número: "))  # Convertimos la entrada a float para manejar decimales

if numero_input > 0:
    print("El número es positivo")
elif numero_input == 0:
    print("El numero es cero")
else:
    print("El número no es positivo")


# Notas:
# - La función input() siempre retorna una cadena; se utiliza float() para conversión.

# =============================================================================
# 64 y 65. Ejercicio Propuesto - Sistema de Descuentos de una Tienda en Línea
# =============================================================================
# En este ejercicio se determina si se aplica un descuento según el valor de compra.
# Requisitos (podemos proponer dos niveles de dificultad):

# Nivel Básico:
# - Si la compra es mayor a 100, aplicar un descuento del 10%, sino el precio se mantiene.

# Nivel Avanzado:
# - Además, si el cliente es "VIP", se aplica un descuento adicional del 5%.
# - Se pueden introducir ambas condiciones (compra y cliente VIP).

# -----------------------------------------------------------------------------
# Solución:
def calcular_descuento(precio: float, es_vip: bool = False) -> float:
    """
    Calcula el precio final aplicando descuentos:
      - Descuento del 10% si precio > 100
      - Descuento adicional del 5% si es VIP

    Parámetros:
        precio (float): Precio original de la compra.
        es_vip (bool): Indicador de si el cliente es VIP (por defecto False).

    Retorna:
        float: Precio final después de aplicar los descuentos.
    """
    precio_final = precio
    if precio > 100:
        precio_final *= 0.90  # Aplica 10% de descuento
    if es_vip:
        precio_final *= 0.95  # Aplica 5% de descuento adicional
    return precio_final


# Ejemplo de uso:
precio_compra = 150.0
cliente_vip = True

print("64/65. Precio final:", calcular_descuento(precio_compra, cliente_vip))
# Puedes probar también con cliente_vip = False y con diferentes precios.

# =============================================================================
# 66. Ejercicio: Sistema Bancario en Python
# =============================================================================
# Ejercicio: Simular una operación bancaria simple.
# Se le pide al usuario ingresar su saldo y un monto a retirar;
# si hay fondos suficientes, se realiza la transacción.

saldo = float(input("Ingrese su saldo: "))
monto_retirar = float(input("Ingrese el monto a retirar: "))

if monto_retirar <= saldo:
    saldo_final = saldo - monto_retirar
    print("Retiro exitoso. Saldo final:", saldo_final)
else:
    print("Fondos insuficientes.")


# =============================================================================
# 67 y 68. Ejercicio Propuesto - El Mayor de dos números en Python
# =============================================================================
# Propuesta: Solicitar dos números al usuario y determinar cuál es el mayor.
# Nivel Básico: Usar if-else para comparar dos números.
# -----------------------------------------------------------------------------
# Solución:
def mayor_de_dos(num1: float, num2: float) -> float:
    """
    Determina el mayor de dos números.

    Parámetros:
        num1 (float): Primer número.
        num2 (float): Segundo número.

    Retorna:
        float: El mayor de los dos números.
    """
    if num1 >= num2:
        return num1
    else:
        return num2


# Ejemplo de uso:
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
print("68. El mayor de los dos es:", mayor_de_dos(n1, n2))

# =============================================================================
# 69. Operador Ternario en Python
# =============================================================================
# El operador ternario permite asignar un valor basado en una condición en una sola línea.
# Sintaxis:
# valor_if_true if condición else valor_if_false

numero_ternario = 8
resultado = "Par" if numero_ternario % 2 == 0 else "Impar"
print("69. El número es:", resultado)


# =============================================================================
# 70 y 71. Ejercicio Propuesto - Estación del Año en Python
# =============================================================================
# Propuesta: Solicitar al usuario el mes (número o nombre) y determinar la estación (verano, otoño, invierno, primavera).
# Nivel Básico: Si se ingresa el mes en número (1 a 12), retornar la estación.
# -----------------------------------------------------------------------------
# Solución:
def obtener_estacion(mes: int) -> str:
    """
    Determina la estación del año dado el número del mes (1 a 12).

    Parámetros:
        mes (int): Número del mes (1-12).

    Retorna:
        str: Estación correspondiente: 'Invierno', 'Primavera', 'Verano' u 'Otoño'.
    """
    if mes in (12, 1, 2):
        return "Invierno"
    elif mes in (3, 4, 5):
        return "Primavera"
    elif mes in (6, 7, 8):
        return "Verano"
    elif mes in (9, 10, 11):
        return "Otoño"
    else:
        return "Mes inválido"


mes_usuario = int(input("Ingrese el número del mes (1-12): "))
print("71. La estación es:", obtener_estacion(mes_usuario))


# =============================================================================
# 72 y 73. Ejercicio Propuesto - Mayor de Edad en Python
# =============================================================================
# Propuesta: Pedir la edad de una persona e indicar si es mayor de edad.
# Nivel sencillo.
# -----------------------------------------------------------------------------
# Solución:
def es_mayor_de_edad(edad: int) -> bool:
    """
    Verifica si la persona es mayor de edad (18 o más).

    Parámetro:
        edad (int): Edad de la persona.

    Retorna:
        bool: True si es mayor de edad, False en caso contrario.
    """
    return True if edad >= 18 else False


edad_persona = int(input("Ingrese su edad: "))
if es_mayor_de_edad(edad_persona):
    print("73. Es mayor de edad")
else:
    print("73. No es mayor de edad")

# =============================================================================
# 74 y 75. Ejercicio Propuesto - Sistema de Calificaciones en Python
