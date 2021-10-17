
# Ejercicio 8.1
import random

l = [('Ola', 'don Pepito'), ('Ola', 'don Jose'), ('Bos', 'días')]

def tuplas_a_diccionario(lista):
    dic = {}
    for i in lista:
        dic.setdefault(i[0], []).append(i[1])
    print(dic)

tuplas_a_diccionario(l)

# Ejercicio 8.2

# 1
cadea = "Que lindo día que fai hoxe que estou moi contento este dia de hoxe"

def texto_a_Diccionario(cadena):
    cadena.lower()
    word = cadena.split(" ")
    dicWords = {}
    for i in word:
        if i.lower() in dicWords:
            dicWords[i.lower()] += 1
        else:
            dicWords[i.lower()] = 1
    print(dicWords)

texto_a_Diccionario(cadea)

# 2

def caracter_a_Diccionario(cadena):
    word = list(cadena)
    dicWords = {}
    for i in word:
        if i.lower() in dicWords:
            dicWords[i.lower()] += 1
        else:
            dicWords[i.lower()] = 1
    print(dicWords)

caracter_a_Diccionario(cadea)

# 3

a = 0
b = 0

def dadosDiccionario():
    num1 = 0
    num2 = 0
    l = []
    dicNum = {}
    for i in range(random.randint(1, 10)):
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        total = (num1 + num2)
        l.append(total)
    print(l)

dadosDiccionario()