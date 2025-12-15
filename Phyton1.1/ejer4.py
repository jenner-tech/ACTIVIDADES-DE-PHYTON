#cadena de texto

mensaje="Bienvenidos al mundo de la programacion en PHYTON"
longitudMensaje=len(mensaje)
print(f"La longitud de {mensaje} es: {longitudMensaje} ")

for letra in mensaje:
    print(letra)
    
print(mensaje[0:4])

if "programacion" in mensaje:
    print("Si existe....")