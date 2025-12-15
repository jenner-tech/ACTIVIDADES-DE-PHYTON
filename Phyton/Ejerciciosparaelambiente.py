#variables
numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))

print("== MENU ==")
print("1.Suma")
print("2.Resta")
print("4.División")
print("5.Salir")

opcion = int(input("Ingrese una opción: "))

if opcion == 1:
    print("La suma de", numero1, "+", numero2, "es:")
    print(numero1 + numero2)

elif opcion == 2:
    print("La resta de", numero1, "-", numero2, "es: ")
    print(numero1 - numero2)

elif opcion == 3:
    print("La multiplicación de", numero1, "*", numero2, "es: ")
    print(numero1 * numero2)

elif opcion == 4:
    print("La Division de", numero1, "/", numero2, "es: ")
    print(numero1 / numero2)

elif opcion == 5:
    print("Saliendo del programa")  
    
 