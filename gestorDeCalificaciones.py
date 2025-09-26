print("----Bienvenida a mi gestor de calificaciones---")
print("°°°°°Menu de opciones°°°°°")
print("1. Calcular promedio simple ")
print("2. Calcular calificacion final  con ponderaciones")
print("3. Mostrar mayor y menor calificacion")
print("4. verificar si apruebas o repruebas")

opcion = input("Ingresa una opcion (1-4): ")

if opcion == "1":
    calificacion1= float(input("Ingrese la primer calificacion: "))
    calificacion2 = float(input("Ingrese la segunda calificacion: "))
    calificacion3 = float(input("Ingrese la tercera calificacion: "))
    promedio = (calificacion1 + calificacion2 + calificacion3) / 3
    print(f"Tu promedio simple es {promedio}")
elif opcion == "2":
    ponderacion1 = float(input("Ingrese el valor de la primer pondercacion: "))
    ponderacion2 = float(input("Ingrese el valor de la segunda pondercacion: "))
    ponderacion3 = float(input("Ingrese el valor de la tercer pondercacion: "))
    calificacion1= float(input("Ingrese la primer calificacion: "))
    calificacion2 = float(input("Ingrese la segunda calificacion: "))
    calificacion3 = float(input("Ingrese la tercera calificacion: "))
    ponderacionEnt1 = ponderacion1/100
    ponderacionEnt2 = ponderacion2/100
    ponderacionEnt3 = ponderacion3/100
    promedioPonderado = (calificacion1*ponderacionEnt1)+(calificacion2*ponderacionEnt2)+(calificacion3*ponderacionEnt3)
    print(f"El promedio ponderado es igual a {promedioPonderado} ")
elif opcion == "3":
    calificacion1= float(input("Ingrese la primer calificacion: "))
    calificacion2 = float(input("Ingrese la segunda calificacion: "))
    calificacion3 = float(input("Ingrese la tercera calificacion: "))
    numMayor = calificacion1
    numMenor = calificacion1
    if calificacion2>numMayor:
        numMayor = calificacion2
    if calificacion3>numMayor:
        numMayor = calificacion3

    if calificacion2<numMenor:
        numMenor = calificacion2
    if calificacion3<numMenor:
        numMenor = calificacion3
    print(f"La calificacion mas alta que obtuviste es {numMayor}")
    print(f"La calificacion mas baja que obtuviste es {numMenor}")

elif opcion == "4":
    caliFinal = float( input("Ingresa tu calificacion final (0-10) "))
    if caliFinal >= 7:
        print("Felicidades aprobaste el curso =)")
    elif caliFinal < 7:
        print("Lo siento reprobaste =(")
    else:
        print("califiacion invalida vuelve a intentar")

else:
    print("La opcion que ingresaste es invalida ADIOS")