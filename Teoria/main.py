def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')

'''Tipos de datos'''
numero = 5
comaFlotante = 24.42
complexos = 7 + 2j
booleanos = True
cadeas = "Cadeas de texto"
cadeas2 = "Otro texto"

print(type(complexos))
print(type(booleanos))
print(str(complexos))
print(cadeas + " " + cadeas2)

'''Operadores'''
#Exponente
numero = 5 ** 5
print(numero)
#Division
div = 5.5 / 2
print(div)
#Division entera
divEntero = 5.5 // 2
print(divEntero)
#Modulo
modulo = 5.5 % 2
print(modulo)

'''Operaciones a nivel de bits'''
binario = 3 & 2
print(binario)
loxica = 3 | 2
print(loxica)
resultado = 3 ^ 2
print(resultado)
resultado2 = ~ 7
print(resultado2)
resultado3 = ~- 7
print(resultado3)
resultado4 = ~+ 7
print(resultado4)
resultado5 = 255 >> 1
print(resultado5)
resultado5 = 255 << 1
print(resultado5)

#Cadenas
cadena1 = "Ola"
cadena2 = "Adios"
cadena = cadena1 * 3
print(cadena)

#Listas

l = [1,2,3,4,5,6,7,8,9,10,11,12]
l2 = [1,"Dous",3+4j,2.34,[1,2,3]]
print(l[2])
print(l2[1])
print(l[-2])
print(l2[-1][1])
print(l2[1][2])

l[2] = 15
print(l)

print(l[1:4])
print(l[1:-1:3])
print(l[1::2])
print(l[:6])
l[4:6] = ["Tres", "Catro", "Cinco"]
print(l)
l[2:5] = ["Cero"]
print(l)

l3 = list()
l4 = []
l3.append(0)
l4.append(1)

#Tupla
t = (1,2, "Tres", [4,5,2+4j])
print(t)
t2 = 2,
print(t2)
print(t[0])
t[3][1] = 9
print(t)

#Recorrer arrays
for elemento in t:
    print(elemento)


#Diccionario

d = {1: "Un",
     2: "Dous",
     3: "Tres",
     "Manuel":"2525545"
     }
print(d)
print(d["Manuel"])
d["Manuel"] = "1424654"
print(d["Manuel"])

print(d.items())
print(d.keys())
print(d.values())
print(d.get("Manuela", "Clave no encontrada"))
print(len(d))

l.append(500)
l.extend((20,21,22,23,24,25,26))
print(l.index(10))
l.insert(10, 113)
print(l.pop(10))
l.remove(10)
l.reverse()
l5 = [2,5,8,6]
l5.sort()
print(l5)
print(l)
#Contar la cantidad de veces que aparece un elemento
print(l.count(1))
print(len(l))

lista = ["Ola", "Adios", "Hasta mañana"]

def ordea(x):
    return len(x)
lista.sort()
print(lista)

#Cadenas de caracteres

cadea = "Python para todos"

print(cadea[3])
print(cadea[3:10])
print(cadea[3:18:2])

print(cadea.count('o'))
print(len(cadea))
print(cadea.find('o', 5, 14))

cadea2 = cadea.join(('Ola', 'a ', 'todos', 'no', 'presente', 'curso'))
print(cadea2)
print(cadea.partition(' '))
print(cadea.split(' '))
print(cadea.replace(' ', '_'))