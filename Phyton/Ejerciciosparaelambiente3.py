numero = int(input("Ingrese numero para mostrar su tabla de multiplicar: "))

print(f"Tabla de multiplicar del numero {numero}")

for i in range(1,11):
    print(f"{numero} * {i} = {numero*i}")