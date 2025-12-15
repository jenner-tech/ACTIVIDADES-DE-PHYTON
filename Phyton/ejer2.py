nombreEstudiante = input("Ingrese nombre del estudiante")
nota1 = float(input("Ingrese la primera nota del estudiante: "))
nota2 = float(input("Ingrese la segunda nota del estudiante: "))
nota3 = float(input("Ingrese la tercera nota del estudiante: "))
notapromedio = (nota1 + nota2 + nota3)/ 3

if notapromedio >= 3.0:
    print("Aprobo y su promedio fue de: ", notapromedio )
else :
    print("Reprobo y su promedio fue de: ", notapromedio)