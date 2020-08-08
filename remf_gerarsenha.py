#!/usr/bin/python3
# pip3 install pyfiglet
# pip3 install colorama

import os, sys, string
import pyfiglet
import colorama
from colorama import Fore, Style
from random import random, choice

def enumero(valor):
    try:
         float(valor)
    except ValueError:
         return False
    return True

def ajuda():
    print(' '+Fore.CYAN)
    print(' Use:', sys.argv[0], '1-6 [ TAMANHO ]')
    print(' Use:', sys.argv[0], '0 [ TAMANHO ] "CARACTERES"')
    print('\n')
    print('       1 = ALFABETO + NUMEROS + CARACTERES ESPECIAIS')
    print('       2 = ALFABETO')
    print('       3 = ALFABETO + NUMEROS')
    print('       4 = ALFABETO + CARACTERES ESPECIAIS')
    print('       5 = NUMEROS + CARACTERES ESPECIAIS')
    print('       6 = CARACTERES ESPECIAIS')
    print('         = NUMEROS')
    print(Style.RESET_ALL+' ')
    quit()

def checar_char(tipo):
    if tipo == 1:
        valores = string.ascii_letters
        valores += string.digits
        valores += string.punctuation
    elif tipo == 2:
        valores = string.ascii_letters
    elif tipo == 3:
        valores = string.ascii_letters
        valores += string.digits
    elif tipo == 4:
        valores = string.ascii_letters
        valores += string.punctuation
    elif tipo == 5:
        valores = string.digits
        valores += string.punctuation
    elif tipo == 6:
        valores = string.punctuation
    else:
        valores = string.digits

    return valores

def gerar_senha(t, tamanho, caracteres):
    if not enumero(t) or not enumero(tamanho):
        ajuda()

    if int(t) == 0:
        if len(caracteres) > 0:
            valores = caracteres
        else:
            ajuda()
    else:
        valores = checar_char(int(t))
        
    senha = ''

    for i in range(int(tamanho)):
        senha += choice(valores)

    return senha
    

def main():
    if len(sys.argv) > 1:
        if len(sys.argv) == 4:
            print(gerar_senha(sys.argv[1], sys.argv[2], sys.argv[3]))
        elif len(sys.argv) == 3:
            print(gerar_senha(sys.argv[1], sys.argv[2], ''))
        else:
            ajuda()
    else:
        ajuda()

if __name__ == "__main__":
    main()
