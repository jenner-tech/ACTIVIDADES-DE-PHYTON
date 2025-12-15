paises =[] #lista vacia

print(f"Lista Actual {paises}")
paises.append("Colombia") #agregar un pais a la lista
print(f"Lista Actual {paises}")
paises.append("Venezuela")
print(f"Lista Actual {paises}")
paises.insert(1, "Peru")
print(f"Lista Actual {paises}")
paises.insert(2, "Peru")
print(f"Lista Actual {paises}")
paises.remove("Peru")
print(f"Lista Actual {paises}")
paises.append("Bolivia")
print(f"Lista Actual {paises}")
paises.append("Ecuador")
print(f"Lista Actual {paises}")

pais  = input("Ingrese Pais: ")
paises.append(pais)
print(f"Lista Actual {paises}")

#Eliminar el ultimo elemento de la lista
paises.pop()
print(f"Lista Actual {paises}")

#eliminar un elemento de acuerdo a la posicion de la lista
paises.pop(1)
print(f"Lista Actual {paises}")

#
#

#Recorrer una lista

for pais in paises:
    print(pais, end="**")
    
longitudpaises = len(paises)
for index in range(len(paises)):
    print(paises[index])

    