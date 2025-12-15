archivo = open("datos.txt","r", encoding="utf-8")
contenido = archivo.read()
print(contenido)
archivo.close()

#procesos crear archivo modo w - sobreescribe el archivo
with open("Salida.txt","w",encoding="utf-8") as archivo:
    archivo.write("Bienvenidos al Sena") 
    archivo.write("\n") #salto de linea
    archivo.write("Hola a todos  desde el CTPI - CAUCA")
    archivo.write("\n")
    archivo.write("Felicitación a todos....")
    archivo.close()
    

#lectura de archivo usando try except y el metodo readlines

try:
    archivo = open ("salida.txt","r", encoding="utf-8")
    lineas = archivo.readlines()
    print(type(lineas))
    print(lineas)
    for linea in lineas:
        print(linea)
        
except IOError as error:
    print("Archivo no existe")
    