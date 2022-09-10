# Calculadora con menú

from math import log 

print("-------------------------------------------")
print("-----------CALCULADORA - MENU--------------")
print("-------------------------------------------")

# input
bandera = False
x = float(input("Dame el valor del número x: "))
y = float(input("Dame el valor del número y: "))


print("\nDame la opción que deseas realizar: \n")
# Se despliega el menú para seleccionar la opción que deseas realizar:
print("1. Sumar (El primero más el segundo)")
print("2. Restar (El primero menos el segundo)")
print("3. Multiplicar (El primero por el segundo)")
print("4. Dividir (El primero sobre el segundo)")
print("5. Potencia (El primero a la potencia del segundo)")
print("6. Logaritmo (El logaritmo del primero)")

opcion = int(input("\nDame la opción: "))