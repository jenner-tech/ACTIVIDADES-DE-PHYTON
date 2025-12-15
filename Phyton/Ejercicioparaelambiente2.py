#variables
nombre = input("Ingrese su nombre: ")
nota1 = float(input("Ingrese su primera nota: "))
nota2 = float(input("Ingrese su segunda nota: "))
nota3 = float(input("Ingrese su tercera nota: "))
promedio = (nota1 + nota2 + nota3)/3

if promedio>= 3.0:
    print("Apobaste felicidades, tu promedio fue de: ", promedio)
else:
    print("No aprobaste que lastima, tu aprobaste fue de: ", promedio)