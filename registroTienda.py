pepe = input("Ingrese el nombre del producto (FIN para terminar): ")

paco = 0
lola = 0
caja = 0
pago = 0

while pepe != "FIN":
    num = int(input("Ingrese la cantidad: "))
    toto = float(input("Ingrese el precio unitario: "))

    paco += 1

    suma = num * toto
    rebaja = 0

    if suma >= 100000:
        rebaja = suma * 0.10
        lola += 1
    elif suma >= 50000:
        rebaja = suma * 0.05
        lola += 1

    final = suma - rebaja

    print("\nProducto:", pepe)
    print("Valor original: $", suma, sep="")
    print("Descuento: $", rebaja, sep="")
    print("Valor a pagar: $", final, sep="")

    caja += suma
    pago += final

    pepe = input("\nIngrese el nombre del producto (FIN para terminar): ")

print("\n--- RESUMEN DE LA COMPRA ---")
print("Productos registrados:", paco)
print("Productos con descuento:", lola)
print("Valor original de las compras: $", caja, sep="")
print("Valor final a pagar: $", pago, sep="")
