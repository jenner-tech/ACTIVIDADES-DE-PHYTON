#agregar datos a n archivo

texto = input("Ingrese texto para agregar al archivo salida.txt: ")

with open("salida.txt","a", encoding="utf-8") as archivo:
    texto = input("Ingrese texto para agregar al archivo salida.txt: ")
    archivo.write(f"{texto}\n")
    print("Se ha modificado el archivo")
    
    