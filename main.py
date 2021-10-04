# Ejercicio 7.1
tuple = (4,3,2,1)
tuple2 = (1,2,3,4)

def ordenar(tuple):
    if tuple[0] > tuple[1]:
        print("De mayor a menor")
    elif tuple[0] < tuple[1]:
        print("De menor a mayor")

ordenar(tuple)
ordenar(tuple2)

#Ejercicio 7.2

t1 = (3,4)
t2 = (4,5)

# 1
def domino1(t1, t2):
    if t1[1] == t2[0] or t1[1] == t2[1]:
        print("Encaja")
    else:
        print("No encaja")

domino1(t1, t2)

# 2
l1 = "3,4"
l2 = "2,5"


def domino2(l1, l2):
    li1 = l1.split(",")
    li2 = l2.split(",")

    if li1 == li2[0] or li1[1] == li2[1]:
        print("Encaja")
    else:
        print("No encaja")


domino2(l1, l2)
#Ejercicio 7.3
# 1

tu = ("Fran", "Javier", "Lucia", "Lucas", "Ana")
def campañaElectoral (tuple):
    for n in tuple:
        print(n + ": Estimado")

campañaElectoral(tu)
print("\t")

# 2
def campañaElectoral2 (tuple, p, number):
    for index,n in enumerate(tuple):
        if p <= index < p + number:
            print(n + ": Estimado")

campañaElectoral2(tu, 1, 2)
print("\t")
# 3
tu2 = (("Fran", "Masculino"), ("Javier", "Masculino"), ("Lucia", "Femenino"), ("Lucas", "Masculino"), ("Ana", "Femenino"))
def campañaElectoral3 (tuple):
    for num in tuple:
        if tuple[1][1] == "Masculino":
            print(num[0] + ": Estimado Masculino")
        elif tuple[1][1] == "Femenino":
            print(num[0] + ": Estimado Femenino")

def campañaElectoral4 (tuple, p, number):
    for index,num in enumerate(tuple):
        if p <= index < p + number:
            if tuple[1][1] == "Masculino":
                print(num[0] + ": Estimado Masculino")
            elif tuple[1][1] == "Femenino":
                print(num[0] + ": Estimado Femenino")

campañaElectoral3(tu2)
print("\t")
campañaElectoral4(tu2, 0, 2)
print("\t")

#Ejercicio 7.5
l = []
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# 1
def primos(l, l2):
    for n in l2:
        c = 0
        for i in range(1, n):
            if n % i == 0:
                c += 1
        if c == 1:
            l.append(n)


primos(l, l2)
print(l)

# 2
print(sum(l2))
print(sum(l2) / len(l2))


# 3
l3 = []
def factorial(l, l2):
    for n in l2:
        fact = n
        for num in range(1, n + 1):
            fact *= num
        l.append(fact)

factorial(l3, l2)
print(l3)