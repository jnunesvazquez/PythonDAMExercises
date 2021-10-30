
#Ejercicio 6.1

# 1
cadea1 = "Hola, buenos dias"
def inicioCadea (cadea):
    for i in range(0, 2):
        print(cadea[i])

inicioCadea(cadea1)
print("\n")

# 2
def finalCadea (cadea):
    for i in range(-3, -0):
        print(cadea[i])

finalCadea(cadea1)

# 3
def cadeaCada2 (cadea):
    print(cadea[::2])

cadeaCada2(cadea1)

# 4
def cadeaInversa (cadea):
    print(cadea[::-1])

cadeaInversa(cadea1)

# 5
def cadeaInversa2 (cadea):
    print(cadea + cadea[::-1])

cadeaInversa2(cadea1)

#Ejercicio 6.2

# 1
def cadeaSplit (cadea, caracter):
    print(caracter.join(cadea))

cadeaSplit(cadea1, ",")

# 2
def cadeaReplace(cadea, caracter):
    print(cadea.replace(" ", caracter))

cadeaReplace(cadea1, "\_")

# 3
def cadeaReplace2(cadea, caracter):
    for i in cadea:
        cadea = cadea.replace(i, caracter)
    print(cadea)

cadeaReplace2(cadea1, "X")

# 4
def cadeaReplace3(cadea, caracter):
    for i in range(0, len(cadea)):
        texto = caracter.join(cadea)
    print(texto)

cadeaReplace3(cadea1, ".")

#Exercicio 6.6

# 3
def reemprazoVogal (palabra):
    """ordeV = {1:'a',
             2:'e',
             3:'i',
             4:'o',
             5:'u'}"""
    vogais ="aeiou"
    ordeV = { 'a':1,
              'e':2,
              'i':3,
              'o':4,
              'u':5}
    novaPalabra = list()
    for i in range (len (palabra)):
        caracter = palabra[i]
        if caracter in ordeV.keys():
            if ordeV[caracter] == 5 :
                novaPalabra[i] = vogais[0]
            else:
                novaPalabra.append(vogais[ordeV[caracter]])
        else:
            novaPalabra.append(caracter)
    return str(novaPalabra)

print (reemprazoVogal ("frigorifico"))


