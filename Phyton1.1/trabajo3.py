#Listas
def promedio(lista):
    if len(lista) == 0:
        return 0 
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

numeros = [4, 10, 45, 19]
print("El promedio es:", promedio(numeros))
