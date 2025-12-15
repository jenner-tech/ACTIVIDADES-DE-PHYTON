#Funcion que retorna el promedio de los numeros de una lista
def obtenerPromedioLista(numeros):
    """_summary_
    Retorna el promedio de los numeros de una lista

    Args:
        numeros (List): lista de numeros

    Returns:
        float: promedio
    """
    suma=0
    cantidadNumeros = len(numeros)
    
    for numero in numeros:
        suma = suma + numero 
        
    promedio = suma/cantidadNumeros
    
    return promedio
    
#INICIA ALGORITMO
ListaNumeros=[8,1,23,12,19,35]

promedio = obtenerPromedioLista(ListaNumeros)

print(f"El promedio de {ListaNumeros} es {promedio}")