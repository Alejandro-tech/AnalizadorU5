import ply.yacc as yacc
from AnalizadorLexico import tokens
import sys
import ply.lex as lex 
import re

resultado_gramatica = []

precedence = (
    ('right', 'ASIGNAR'),
    ('right', 'VARIABLES'),
    ('right', 'MAYOR'),
    ('right', 'IGUAL'),
    ('right', 'RESTA'),
    ('right', 'FORMULAS'), #CAMBIO NORMAL RECONOCE
    ('right', 'STRING'),
    ('right', 'ESTRUCTURA'), #MARCAN LAS PALABRAS RESERVADAS
)
nombres = {}

def p_declaracion_asignacion(t):
    'declaracion : ASIGNAR'
    t[0] = t[1]

def p_declaracion_variables(t):
    'declaracion : VARIABLES'
    t[0] = t[1]
#DECLARA PERO YA MUESTRA
def p_declaracion_mayor(t):
    'declaracion : MAYOR'
    t[0] = t[1]

def p_declaracion_igual(t):
    'declaracion : IGUAL'
    t[0] = t[1]

def p_declaracion_resta(t):
    'declaracion : RESTA'
    t[0] = t[1]

def p_declaracion_formulas(t):
    'declaracion : FORMULAS'
    t[0] = t[1]

def p_declaracion_string(t):
    'declaracion : STRING'
    t[0] = t[1]
#ESCRUTURA PRINCIPALES SOLO PARA EJEMPLOS
def p_declaracion_estructura(t):
    'declaracion : ESTRUCTURA'
    t[0] = t[1]
#VERIFICA LA EXISTENCIA DE ERRORES      FUNCIONAMIENTO VERIFICADO CORRECTO
def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {:4} en el valor {:4}".format(
            str(t.type), str(t.value))
    else:
        resultado = "Error sintactico {}".format(t)
    resultado_gramatica.append(resultado)

parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
   
    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("")
    return resultado_gramatica
# ARCHIVO COMPLETO CON EJEMPLOS
try:
    file_name = sys.argv[1]
    archivo = open(file_name, "r")
except:
    print("el archivo no se encontro")
    quit()

text = ""
for linea in archivo:
    text += linea

