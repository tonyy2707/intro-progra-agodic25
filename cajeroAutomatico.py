"""
Crea un programa que simule un cajero con un saldo inicial.

Menú con opciones: consultar saldo, retirar, depositar o salir.

Si se retira, verificar que el saldo sea suficiente.

Si se deposita, sumar el monto al saldo.

Mostrar mensajes claros en cada operación.
"""
print("----Bienvenida a mi cajero automatico---")
print("°°°°°Menu de opciones°°°°°")
print("1. Consultar saldo ")
print("2. Retirar efectivo")
print("3. Hacer un deposito")
print("4. Salir")
opcion = input("Ingresa una opcion (1-4): ")

if opcion == "1":
    saldoInicial = 5000
    print(f"Tu saldo es: {saldoInicial} MX")
elif opcion == "2":
    saldoInicial = 5000
    retiro = float(input("Ingrese la cantidad que desea retirar: "))
    if retiro <= saldoInicial :
        retiroFinal = saldoInicial-retiro
        print(f"Tu nuevo saldo es: {retiroFinal} MX ")
    else:
        print("El monto que deseas retirar sobrepasa tu saldo")
elif opcion == "3":
    saldoInicial = 5000
    deposito = float(input("Ingrese el monto que deseas depositar : "))
    nuevoSaldo = saldoInicial+deposito
    print(f"Tu nuevo saldo es {nuevoSaldo} MX")
elif opcion == "4":
    print("Hasta luego :3")
else:
    print("opcion invalida, ejecute de nuevo...")