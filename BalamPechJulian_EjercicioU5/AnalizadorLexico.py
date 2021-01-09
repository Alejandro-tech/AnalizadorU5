import ply.lex as lex
import re
import sys

resultado_lexema = []

#DECLARE VARIABLES STRING Y ESTRUCTURA COMPROBADAS FUNCIONAN BIEN
tokens = [
    'ASIGNAR',
    'VARIABLES',
    'MAYOR',
    'IGUAL',
    'RESTA',
    'FORMULAS',
    'STRING',
    'ESTRUCTURA'
]
#DIO ERROR SOLO POR LA ESTRUCTURA PERO CORREGIDO
def t_ASIGNAR(t):
    r'(\w+\s\=\s(\d+|\w+))'
    return t

def t_VARIABLES(t):
    r'(\w+\=(\d+|\w+)[+*/-](\d+|\w+))'
    return t

def t_MAYOR(t):
    r'\w+\s([<>])\s(\d+|\w+)'
    return t

def t_IGUAL(t):
    r'(\s|\S)\w+\s((\<\=)|(\>\=))\s(\d+|\w+)'
    return t

def t_RESTA(t):
    r'\w+\s((\=\=)|(\!\=))\s\d+'
    return t

def t_FORMULAS(t):
    r'(\w+\s\=\s)(\(\d[+*/-]\d\)[*/+-]\d)|(\w+\=)(\(\w+[/*+-]\d[*/+-]\d\)[/*+-]\w+)'
    return t

def t_ESTRUCTURA(t):
    r'if|while|case|for|else|end'
    return t

def t_STRING(t):
    r'\w+|:'
    return t

t_ignore = '\t'

def t_espacio(t):
    r"\s"
    pass

def t_error(t):
    global resultado_lexema
    estado = "Error de token en linea {:4}".format(str(t.lineno))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Line {:4} Type {:4} Value {:4}".format(
            str(tok.lineno), str(tok.type), str(tok.value))
        resultado_lexema.append(estado)

    return resultado_lexema

analizador = lex.lex()

try:
    file_name = sys.argv[1]
    archivo = open(file_name, "r")
except:
    print("el archivo no se encontro")
    quit()

text = ""
for linea in archivo:
    text += linea
prueba(text)
print('\n'.join(list(map(''.join, resultado_lexema))))