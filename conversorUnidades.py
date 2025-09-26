print("----Bienvenida a mi conversor de unidades---")
print("°°°°°Menu de opciones°°°°°")
print("1. Temperatura ")
print("2. Longitud")
print("3. Masa")
print("4. Salir")

opcion = input("Ingresa la unidad que deseas convertir (1-4) ")

if opcion == "1":
    print("1. Celcius a Fahrenheit")
    print("2. Fahrenheit a Celcius")
    opcion = input("Ingresa una de las opciones (1 o 2): ")
    if opcion == "1":
        celcius = float(input("Ingresa los grados Celcius: "))
        fahrenheit = celcius * 1.8 +32
        print(f"{celcius} grados celcius es equivalente a {fahrenheit} grados Farenheit")
    elif opcion== "2":
        fahrenheit = float(input("Ingrese los grados Fahrenheit: "))
        celcius = (fahrenheit-32)/1.8
        print(f"{fahrenheit} grados Fahrenheit es equivalente a {celcius} grados Celcius")
    else:
        print("La opcion que ingresaste es invalida, ADIOS!!!")
elif opcion == "2":
    print("1. Metros a Centimetros")
    print("2. Centimetros a metros")
    opcion = input("Ingresa una de las dos opciones (1 o 2)")
    if opcion == "1":
        metros = float(input("ingrese los metros: "))
        centimetros = metros * 100
        print(f"{metros} metros es igual a {centimetros} centimetros")
    elif opcion == "2":
        centimetros = float(input("Ingresa los centimetros: "))
        metros = centimetros/100
        print(f"{centimetros} centimetros ees igual a {metros} metros ")
    else:
        print("La opcion ingresada no es valida")
elif opcion == "3":
    print("1. Kilogramos a gramos")
    print("2. Gramos a kilogramos")
    opcion = input("Ingresa una de las dos opciones (1 o 2)")
    if opcion == "1":
        kilos = float(input("Ingrese los kilos: "))
        gramos = kilos * 1000
        print(f"{kilos} kilos es igual a {gramos} gramos")
    elif opcion == "2":
        gramos = float(input("Ingrese los gramos: "))
        kilos = gramos/1000
        print(f"{gramos} gramos es igual a {kilos} kilos")
    else:
        print("La opcion ingresada no es valida")
elif opcion == "4":
    print("Hasta luego :D")
else :
    print("opcion invalida vuelve a intentar :D...")