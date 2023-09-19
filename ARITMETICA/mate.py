import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir entre 0"
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a):
    return math.sqrt(a)

def inverso(a):
    return 1 / a

def seno(a):
    return math.sin(a)

def coseno(a):
    return math.cos(a)

def tangente(a):
    return math.tan(a)

def modulo(a):
    return abs(a)