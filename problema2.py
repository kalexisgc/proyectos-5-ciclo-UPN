"""
Pida el nombre y ruc de un cliente y cree una función que valide que tenga 11 cifras
tal que si falla le indique al usuario que esta mal escrito
"""
def validar_ruc(ruc):
    # Verifica que tenga 11 caracteres y que todos sean números
    if len(ruc) == 11 and ruc.isdigit():
        return True
    else:
        return False


# Programa principal
nombre = input("Ingrese el nombre del cliente: ")
ruc = input("Ingrese el RUC: ")

if validar_ruc(ruc):
    print("\n--- RESULTADO ---")
    print("Cliente:", nombre)
    print("RUC válido")
else:
    print("\nError: El RUC debe tener exactamente 11 dígitos numéricos.")