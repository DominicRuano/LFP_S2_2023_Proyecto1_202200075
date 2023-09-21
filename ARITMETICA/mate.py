import math
from functools import reduce

torad = math.pi/180

def suma(*args):
    return float("{:.2f}".format(sum(args)))

def resta(*args):
    numero = args[0]-sum(args[1:])
    return float("{:.2f}".format(numero))

def multiplicacion(*args):
    numero = 1
    for a in args:
        numero *= a
    return float("{:.2f}".format(numero))

def division(a, b):
    if b == 0:
        return "No se puede dividir entre 0"
    return float("{:.2f}".format(a / b))

def potencia(a, b):
    return float("{:.2f}".format(math.pow(a, b)))

def raiz(a,b):
    if b == 0:
        return "La raiz no puede ser de 0."
    
    resultado = math.pow(a, 1/b)
    return float("{:.2f}".format(resultado))

def inverso(a):
    return float("{:.2f}".format(1 / a))

def seno(a):
    return float("{:.2f}".format(math.sin(a*torad)))

def coseno(a):
    return float("{:.2f}".format(math.cos(a*torad)))

def tangente(a):
    return float("{:.2f}".format(math.tan(a*torad)))

def modulo(a,b):
    return float("{:.2f}".format(a%b))