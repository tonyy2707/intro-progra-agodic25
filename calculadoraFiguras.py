#from math import * #Nos importamos toda la librería
#from math import sqrt, pi #aquí importamos la función de raíz cuadrada y el valor de pi
from math import pi #importamos solo el valor de la constate pi

print("---- Bienvenida a mi Calculadora de Figuras ---")
print("-°-°-°- Menú de figuras -°-°-°-")
print("1. Cubo")
print("2. Prisma")
print("3. Pirámide")
print("4. Cilindro")
print("5. Cono")
print("6. Esfera")

figura = input("Figura (1-6): ")

print("-°-°-°- Menú de opciones -°-°-°-")
print("1. Calcular el área")
print("2. Calcular el volumen")
print("3. Calcular ambos")
print("4. Salir")

opcion = input("Opción (1-4): ")

if opcion == "1": #Este if controla qué quiere el usuario calcular.
    if figura == "1": #Este if anidado controla la figura para calcular el área.
        lado = float(input("Ingresa el lado de la figura (cm):"))
        areaCubo = 6*lado**2
        print(f"El área del cubo es: {areaCubo:.2}")
    elif figura == "2":
        areab = float(input("Ingresa el area de la base (cm): "))
        perimetro = float(input("Ingresa el permietro (cm): "))
        altura = float(input("Ingresa la altura (cm): "))
        areaTotal = 2*areab+perimetro*altura
        print(f"El área del prisma es: {areaTotal:.2}")
    elif figura == "3":
        areab =float(input("Ingresa el area base (cm): "))
        perimetro =float(input("Ingrese el perimetro (cm): "))
        apotema =float(input("Ingresa el apotema (cm): "))
        area = areab*((perimetro*apotema)/2)
        print(f"El área de la piramide es: {area:.2}")
    elif figura == "4":
        radio =float(input("Ingrese el radio de la figura (cm): "))
        altura= float(input("Ingrese la altura de la figura (cm): "))
        area= 2*pi*radio*(radio+altura)
        print(f"El area del cilindro es: {area:.2}")
    elif figura == "5":
        generatriz = float(input("Ingrese la generatriz de la figura (cm): "))
        radio = float(input("Ingrese el radio de la figura (cm): "))
        areaCono = pi*radio*(radio+generatriz)
        print(f"El area del cono es : {areaCono:.2}")
    elif figura == "6":
        radio = float(input("Ingresa el radio de la esfera"))
        areaEsfera = 4*pi*radio**2
        print(f"El area de la esfera  es: {areaEsfera:.2}")
    else:
        print("No conozco esa figura. ")
elif opcion == "2":
    if figura == "1": #Este if aninado controla la figura para calcular el volumen.
        lado = float(input("Lado (cm):"))
        volumenCubo = lado**3
        print(f"El volumen del cubo es: {volumenCubo:.4}")
    elif figura == "2":
         areab = float(input("Ingresa el area de la base (cm): "))
         altura = float(input("Ingresa la altura (cm): "))
         volumenPrisma = areab * altura
         print(f"El volumen del prisma es: {volumenPrisma:.4}")
    elif figura == "3":
        areab = float(input("Ingrese el area base (cm): "))
        altura= float(input("Ingrese la altura (cm): "))
        volumenPiramide = (1/3)*areab*altura
        print(f"El volumen de la piramide es: {volumenPiramide:.4}")
    elif figura == "4":
        radio = float(input("Ingrese eel radio de la figura (cm): "))
        altura =float(input("Ingrese la altura de la figura (cm): "))
        volumenCilindro = pi*radio**2*altura
        print(f"El volumen del cilandrro es {volumenCilindro:.2}")
    elif figura == "5":
        radio = float(input("Ingresa el radio de la figura (cm) : "))
        altura = float(input("Ingresa la altura de la figura (cm) "))
        volumenCono = (1/3)*pi*radio**2*altura
        print(f"El volumen del cono es : {volumenCono:.2}")
    elif figura == "6":
        radio = float(input("Ingrese el radio de la figura (cm): "))
        volumenEsfera = (4/3)*pi*radio**3
        print(f"El volumen de la esfera es : {volumenEsfera:.2}")
    else:
        print("No conozco esa figura. ")
elif opcion == "3":
    if figura == "1": #Este if aninado controla la figura para calcular ambos.
        lado = float(input("Lado (cm):"))
        areaCubo = 6*lado**2
        print(f"El área del cubo es: {areaCubo:.2}")
        volumenCubo = lado**3
        print(f"El volumen del cubo es: {volumenCubo:.2}")
    elif figura == "2":
        areab = float(input("Ingresa el area de la base (cm): "))
        perimetro = float(input("Ingresa el permietro (cm): "))
        altura = float(input("Ingresa la altura (cm): "))
        areaTotal = 2*areab+perimetro*altura
        print(f"El área del prisma es: {areaTotal:.2}")
        volumenPrisma = areab * altura
        print(f"El volumen del prisma es: {volumenPrisma:.4}")
    elif figura == "3":
         areab =float(input("Ingresa el area base (cm): "))
         perimetro =float(input("Ingrese el perimetro (cm): "))
         apotema =float(input("Ingresa el apotema (cm): "))
         altura= float(input("Ingrese la altura (cm): "))
         area = areab*((perimetro*apotema)/2)
         volumenPiramide = (1/3)*areab*altura
         print(f"El área de la piramide es: {area:.2}")
         print(f"El volumen de la piramide es: {volumenPiramide:.4}")
    elif figura == "4":
        radio =float(input("Ingrese el radio de la figura (cm): "))
        altura= float(input("Ingrese la altura de la figura (cm): "))
        area= 2*pi*radio*(radio+altura)
        volumenCilindro = pi*radio**2*altura
        print(f"El area del cilindro es: {area:.2}")
        print(f"El volumen del cilandrro es {volumenCilindro:.2}")
    elif figura == "5":
        generatriz = float(input("Ingrese la generatriz de la figura (cm): "))
        radio = float(input("Ingrese el radio de la figura (cm): "))
        areaCono = pi*radio*(radio+generatriz)
        altura = float(input("Ingresa la altura de la figura (cm) "))
        volumenCono = (1/3)*pi*radio**2*altura
        print(f"El area del cono es : {areaCono:.2}")
        print(f"El volumen del cono es : {volumenCono:.2}")
    elif figura == "6":
        radio = float(input("Ingrese el radio de la figura (cm): "))
        volumenEsfera = (4/3)*pi*radio**3
        areaEsfera = 4*pi*radio**2
        print(f"El area de la esfera  es: {areaEsfera:.2}")
        print(f"El volumen de la esfera es : {volumenEsfera:.2}")
    else:
        print("No conozco esa figura. ")
elif opcion == "4":
    print("Hastal luego =)")
else:
    print("Opción incorrecta, adiós. =D")