""" Pida el nombre del cliente, cuantas manzanas comprara y un precio. 
Muestre el nombre y el total a pagar """
try:
    nombre = input("Ingrese el nombre del cliente: ")

    cantidad = int(input("¿Cuántas manzanas comprará?: "))
    precio = float(input("Ingrese el precio de cada manzana: "))

    total = cantidad * precio

    print("\n--- RESULTADO ---")
    print("Cliente:", nombre)
    print("Total a pagar: S/ {:.2f}".format(total))

except ValueError:
    print("Error: Debes ingresar números válidos en cantidad y precio.")