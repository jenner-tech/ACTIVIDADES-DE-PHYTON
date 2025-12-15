tupla = ("Manzana", "Banana", "Cereza", 10, True)

# 2. Acceder a elementos por su índice
print(f"Primer elemento: {tupla[0]}")  # Salida: Manzana
print(f"Último elemento: {tupla[-1]}") # Salida: True

# 3. Desempaquetado de tuplas
frutas = ("Pera", "Uva", "Mango")
(verde, morada, dulce) = frutas
print(f"La fruta dulce es: {dulce}")

# 4. Longitud de la tupla
print(f"Cantidad de elementos: {len(tupla)}")

# 5. Intentar modificar una tupla (Esto dará un ERROR)
try:
    tupla[0] = "Fresa"
except TypeError as e:
    print(f"\nError esperado: {e}")
    print("Recuerda: Las tuplas no se pueden modificar.")