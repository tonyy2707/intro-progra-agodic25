print("----Bienvenida a mi Tienda/Cotizador simple---")
print("°°°°°Menu de opciones°°°°°")
print("1. Calcular el total con IVA ")
print("2. Calcular Total con descuento + IVA")
print("3. Calcular precio unitario")
print("4. Salir")

opcion = input("Ingresa una opcion del menu (1-4): ")

if opcion == "1" : 
    precio = float(input("Ingrese el precio del articulo: "))
    cantidad = float(input("Ingrese la cantidad de articulos: "))
    totalIVA= (precio*cantidad)*(1+.16)
    print(f"El precio total con IVA es {totalIVA}")
elif opcion == "2" :
    precio = float(input("Ingrese el precio del articulo: "))
    cantidad = float(input("Ingrese la cantidad de articulos: "))
    descuento = float(input("Ingrese el descuento del procuto: "))
    precioDescuento = (precio*cantidad)*(1-descuento/100)
    totalIVA= precioDescuento*(1+.16)
    print(f"El precio total con descuento + IVA es: {totalIVA}")
elif opcion == "3" :
    total = float(input("Ingrese el total de la compra: "))
    cantidad = float(input("Ingrese la cantidad de articulos comprados: "))
    precioUnitario = total/cantidad
    print(f"El precio unitario es: {precioUnitario}")
elif opcion == "4" :
    print("HASTA LUEGO =).....")
else:
    print("La opcion que ingresaste no es valida, vuelve a intentar")