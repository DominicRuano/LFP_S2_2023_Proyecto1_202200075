import math

torad = math.pi/180

def suma(*args):
    return sum(args)

def resta(*args):
    numero = 0
    for a in args:
        numero -= a
    return numero

def multiplicacion(*args):
    numero = 0
    for a in args:
        numero *= a
    return numero

def division(a, b):
    if b == 0:
        return "No se puede dividir entre 0"
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a,b):
    if b == 0:
        return "La raiz no puede ser de 0."
    
    resultado = math.pow(a, 1/b)
    return resultado

def inverso(a):
    return 1 / a

def seno(a):
    return math.sin(a*torad)

def coseno(a):
    return math.cos(a*torad)

def tangente(a):
    return math.tan(a*torad)

def modulo(a):
    return abs(a)