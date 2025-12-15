#>4.5 Excelente
#>4 y <= 4.5 Muy bien
#>= 3 y <=4 Aceptable
#<3 Reprobado

nota = float(input("Ingrese nota no mayor a 5 "))

if nota > 4.5:
    print("Excelente...")
elif nota >4 and nota<=4.5:
    print("Muy bien...")
elif nota >=3 and nota<=4:
    print("Aceptable...")
else:
    print("Reprobado...")
