archivo = open("datos.txt","r", encoding="utf-8")
contenido = archivo.read()
print(contenido)
archivo.close()