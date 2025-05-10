# Area and perimeter calculator
print("Bienvenido a la calculadora de Áreas y perímetros de Rectangulos y circulos :)")

def area_rectangulo(base, altura):
    area = base * altura
    return area

def perimetro_rectangulo(base, altura):
    perimetro = 2*(base + altura)
    return perimetro

def area_circulo(radio):
    area = ((radio**2)*(3.14))
    return area

def perimetro_circulo(radio):
    perimetro = 2*(3.14*radio)
    return perimetro

def obtener_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor ingresa un número: ")


quiere_salir = False
while not quiere_salir:
    print("[1] Rectángulo\n[2] Círculo")
    seleccion = input("Selecciona tu opción: ")
    if seleccion == "1":
        print("[1] Área Rectángulo\n[2] Perimetro Rectángulo")
        opcion = input("Selecciona tu opcion: ")
        if opcion == "1":
            base = obtener_float("Largo de la base: ")
            largo = obtener_float("Largo de la altura: ")
            area = area_rectangulo(base, largo)
            print(f"El área del Rectángulo es: {area}")
            opcion_salir = input("Quieres continuar? (yes o no): ").lower()
            if opcion_salir == "yes":
                quiere_salir = False
            elif opcion_salir == "no":
                quiere_salir = True
        elif opcion == "2":
            base = obtener_float("Largo de la base : ")
            largo = obtener_float("largo de la altura : ")
            perimetro = perimetro_rectangulo(base, largo)
            print(f"El perímetro es: {perimetro}")
            opcion_salir = input("Quieres continuar? (Yes or No): ").lower()
            if opcion_salir == "yes":
                quiere_salir = False
            elif opcion_salir == "no":
                quiere_salir = True
        else:
            print("Por favor ingresa una opción valida.")
    elif seleccion == "2":
        print("[1] Área Círculo\n[2] Perímetro Círculo")
        opcion = input("Selecciona tu opcion: ")
        if opcion == "1":
            radio = obtener_float("Radio: ")
            area = area_circulo(radio)
            print(f"El área es: {area}")
            opcion_salir = input("Quieres continuar? (Yes or No): ").lower()
            if opcion_salir == "yes":
                quiere_salir = False
            elif opcion_salir == "no":
                quiere_salir = True
        elif opcion == "2":
            radio = obtener_float("Radio: ")
            perimetro = perimetro_circulo(radio)
            print(f"El perímetro es: {perimetro}")
            opcion_salir = input("Quieres continuar? (Yes or No): ").lower()
            if opcion_salir == "yes":
                quiere_salir = False
            elif opcion_salir == "no":
                quiere_salir = True
        else:
            print("Por favor ingresa una opción valida.")
    else:
        print("Por favor ingresa una opción valida.")