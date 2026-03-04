# ─────────────────────────────────────────────────────────────────────────────
# Base de ejercicios Python 3 — fuente: ayudantía USM progra.usm.cl
# Estructura: lista de categorías, cada una con lista de ejercicios
# Cada ejercicio: titulo, url_enunciado, enunciado, ejemplo_io, codigo
# ─────────────────────────────────────────────────────────────────────────────

EJERCICIOS = [
    {
        "categoria": "Parte I — Programas Simples",
        "icono": "🟢",
        "ejercicios": [
            {
                "titulo": "Saludo",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/saludo.html",
                "enunciado": "Escriba un programa que pida al usuario que escriba su nombre, y lo salude llamándolo por su nombre.",
                "ejemplo": "Ingrese su nombre: Perico\nHola, Perico",
                "codigo": '''\
# Saludo
nombre = input("Ingrese su nombre: ")
print("Hola,", nombre)
'''
            },
            {
                "titulo": "Círculo",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/circulo.html",
                "enunciado": "Escriba un programa que reciba el radio de un círculo y entregue su perímetro y su área.",
                "ejemplo": "Radio: 5\nPerímetro: 31.41592653589793\nÁrea: 78.53981633974483",
                "codigo": '''\
# Círculo
import math

radio = float(input("Radio: "))
perimetro = 2 * math.pi * radio
area = math.pi * radio ** 2
print("Perímetro:", perimetro)
print("Área:", area)
'''
            },
            {
                "titulo": "Promedio",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/promedio.html",
                "enunciado": "Escriba un programa que pida tres notas al usuario y muestre el promedio de ellas.",
                "ejemplo": "Nota 1: 55\nNota 2: 71\nNota 3: 48\nPromedio: 58.0",
                "codigo": '''\
# Promedio de tres notas
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
promedio = (nota1 + nota2 + nota3) / 3
print("Promedio:", promedio)
'''
            },
            {
                "titulo": "Temperatura",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/temperatura.html",
                "enunciado": "Escriba un programa que convierta una temperatura de grados Celsius a Fahrenheit.\nLa fórmula es: F = (9/5) × C + 32",
                "ejemplo": "Temperatura en Celsius: 100\nTemperatura en Fahrenheit: 212.0",
                "codigo": '''\
# Conversión Celsius → Fahrenheit
celsius = float(input("Temperatura en Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print("Temperatura en Fahrenheit:", fahrenheit)
'''
            },
            {
                "titulo": "Hipotenusa",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/hipotenusa.html",
                "enunciado": "Escriba un programa que pida los catetos de un triángulo rectángulo y entregue la longitud de la hipotenusa.",
                "ejemplo": "Cateto a: 3\nCateto b: 4\nHipotenusa: 5.0",
                "codigo": '''\
# Hipotenusa (Teorema de Pitágoras)
import math

a = float(input("Cateto a: "))
b = float(input("Cateto b: "))
hipotenusa = math.sqrt(a**2 + b**2)
print("Hipotenusa:", hipotenusa)
'''
            },
            {
                "titulo": "Tiempo",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/tiempo.html",
                "enunciado": "Escriba un programa que pida un número de segundos y lo exprese en horas, minutos y segundos.",
                "ejemplo": "Ingrese segundos: 9814\n2 horas, 43 minutos, 34 segundos",
                "codigo": '''\
# Conversión de segundos a horas, minutos y segundos
t = int(input("Ingrese segundos: "))
horas = t // 3600
minutos = (t % 3600) // 60
segundos = t % 60
print(f"{horas} horas, {minutos} minutos, {segundos} segundos")
'''
            },
        ]
    },
    {
        "categoria": "Parte I — Estructuras Simples",
        "icono": "🔵",
        "ejercicios": [
            {
                "titulo": "Valor absoluto",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/valor-absoluto.html",
                "enunciado": "Escriba un programa que pida un número y muestre su valor absoluto, sin usar la función abs().",
                "ejemplo": "Ingrese un número: -7\nValor absoluto: 7",
                "codigo": '''\
# Valor absoluto sin usar abs()
numero = float(input("Ingrese un número: "))
if numero < 0:
    resultado = -numero
else:
    resultado = numero
print("Valor absoluto:", resultado)
'''
            },
            {
                "titulo": "Clasificar triángulo",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/triangulo.html",
                "enunciado": "Escriba un programa que pida los tres lados de un triángulo y lo clasifique como equilátero, isósceles o escaleno.",
                "ejemplo": "Lado a: 5\nLado b: 5\nLado c: 3\nTriángulo isósceles",
                "codigo": '''\
# Clasificar triángulo
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

if a == b == c:
    print("Triángulo equilátero")
elif a == b or b == c or a == c:
    print("Triángulo isósceles")
else:
    print("Triángulo escaleno")
'''
            },
            {
                "titulo": "Mayor de tres",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/mayor-tres.html",
                "enunciado": "Escriba un programa que pida tres números y muestre el mayor de ellos.",
                "ejemplo": "Número 1: 14\nNúmero 2: 8\nNúmero 3: 21\nEl mayor es: 21",
                "codigo": '''\
# Mayor de tres números
a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))

if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
else:
    mayor = c

print("El mayor es:", mayor)
'''
            },
            {
                "titulo": "IMC",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/imc.html",
                "enunciado": "Escriba un programa que calcule el Índice de Masa Corporal (IMC) de una persona y lo clasifique.\nIMC = peso(kg) / estatura(m)²",
                "ejemplo": "Peso (kg): 70\nEstatura (m): 1.75\nIMC: 22.86\nClasificación: Normal",
                "codigo": '''\
# Índice de Masa Corporal (IMC)
peso = float(input("Peso (kg): "))
estatura = float(input("Estatura (m): "))
imc = peso / estatura**2
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Clasificación: Bajo peso")
elif imc < 25:
    print("Clasificación: Normal")
elif imc < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")
'''
            },
        ]
    },
    {
        "categoria": "Parte I — Ciclos",
        "icono": "🟡",
        "ejercicios": [
            {
                "titulo": "Tabla de multiplicar",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/tabla.html",
                "enunciado": "Escriba un programa que pida un número entero y muestre su tabla de multiplicar del 1 al 10.",
                "ejemplo": "Número: 7\n7 x 1 = 7\n7 x 2 = 14\n...\n7 x 10 = 70",
                "codigo": '''\
# Tabla de multiplicar
n = int(input("Número: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
'''
            },
            {
                "titulo": "Factorial",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/factorial.html",
                "enunciado": "Escriba un programa que calcule el factorial de un número entero positivo ingresado por el usuario.",
                "ejemplo": "Ingrese un número: 5\n5! = 120",
                "codigo": '''\
# Factorial
n = int(input("Ingrese un número: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")
'''
            },
            {
                "titulo": "Suma de dígitos",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/suma-digitos.html",
                "enunciado": "Escriba un programa que pida un número entero positivo y calcule la suma de sus dígitos.",
                "ejemplo": "Ingrese un número: 4815\nSuma de dígitos: 18",
                "codigo": '''\
# Suma de dígitos
numero = input("Ingrese un número: ")
suma = 0
for digito in numero:
    suma += int(digito)
print("Suma de dígitos:", suma)
'''
            },
            {
                "titulo": "Números primos",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/primos.html",
                "enunciado": "Escriba un programa que determine si un número ingresado por el usuario es primo o no.",
                "ejemplo": "Ingrese un número: 17\n17 es primo",
                "codigo": '''\
# Número primo
n = int(input("Ingrese un número: "))
es_primo = n > 1
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        es_primo = False
        break

if es_primo:
    print(f"{n} es primo")
else:
    print(f"{n} no es primo")
'''
            },
            {
                "titulo": "Fibonacci",
                "url": "http://progra.usm.cl/apunte/ejercicios/1/fibonacci.html",
                "enunciado": "Escriba un programa que muestre los primeros n términos de la sucesión de Fibonacci.",
                "ejemplo": "¿Cuántos términos? 8\n0 1 1 2 3 5 8 13",
                "codigo": '''\
# Sucesión de Fibonacci
n = int(input("¿Cuántos términos? "))
a, b = 0, 1
terminos = []
for _ in range(n):
    terminos.append(str(a))
    a, b = b, a + b
print(" ".join(terminos))
'''
            },
        ]
    },
    {
        "categoria": "Parte II — Funciones y Módulos",
        "icono": "🟣",
        "ejercicios": [
            {
                "titulo": "Función máximo",
                "url": "http://progra.usm.cl/apunte/ejercicios/2/maximo.html",
                "enunciado": "Escriba una función llamada maximo(a, b) que retorne el mayor de dos números. Luego úsela en un programa.",
                "ejemplo": "Número 1: 34\nNúmero 2: 91\nEl máximo es: 91",
                "codigo": '''\
# Función máximo
def maximo(a, b):
    if a >= b:
        return a
    else:
        return b

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
print("El máximo es:", maximo(n1, n2))
'''
            },
            {
                "titulo": "Función es_par",
                "url": "http://progra.usm.cl/apunte/ejercicios/2/es-par.html",
                "enunciado": "Escriba una función es_par(n) que retorne True si n es par y False si es impar. Úsela para clasificar un número ingresado.",
                "ejemplo": "Ingrese un número: 14\n14 es par",
                "codigo": '''\
# Función es_par
def es_par(n):
    return n % 2 == 0

numero = int(input("Ingrese un número: "))
if es_par(numero):
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
'''
            },
            {
                "titulo": "Función potencia",
                "url": "http://progra.usm.cl/apunte/ejercicios/2/potencia.html",
                "enunciado": "Escriba una función potencia(base, exponente) que calcule base^exponente usando un ciclo (sin usar el operador **).",
                "ejemplo": "Base: 3\nExponente: 4\nResultado: 81",
                "codigo": '''\
# Potencia sin usar **
def potencia(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

base = int(input("Base: "))
exp = int(input("Exponente: "))
print("Resultado:", potencia(base, exp))
'''
            },
        ]
    },
    {
        "categoria": "Parte II — Listas",
        "icono": "🟠",
        "ejercicios": [
            {
                "titulo": "Promedio de lista",
                "url": "http://progra.usm.cl/apunte/ejercicios/2/promedio-lista.html",
                "enunciado": "Escriba un programa que pida al usuario ingresar números hasta que escriba 'fin', y luego muestre el promedio.",
                "ejemplo": "Ingrese número (o 'fin'): 4\nIngrese número (o 'fin'): 8\nIngrese número (o 'fin'): fin\nPromedio: 6.0",
                "codigo": '''\
# Promedio de lista dinámica
numeros = []
while True:
    entrada = input("Ingrese número (o 'fin'): ")
    if entrada == "fin":
        break
    numeros.append(float(entrada))

if numeros:
    promedio = sum(numeros) / len(numeros)
    print("Promedio:", promedio)
else:
    print("No ingresó ningún número.")
'''
            },
            {
                "titulo": "Invertir lista",
                "url": "http://progra.usm.cl/apunte/ejercicios/2/invertir-lista.html",
                "enunciado": "Escriba un programa que pida 5 números, los guarde en una lista y los muestre en orden inverso.",
                "ejemplo": "Número 1: 3\nNúmero 2: 7\nNúmero 3: 1\nNúmero 4: 9\nNúmero 5: 4\nInverso: [4, 9, 1, 7, 3]",
                "codigo": '''\
# Invertir lista
numeros = []
for i in range(1, 6):
    n = float(input(f"Número {i}: "))
    numeros.append(n)

print("Inverso:", numeros[::-1])
'''
            },
        ]
    },
]
