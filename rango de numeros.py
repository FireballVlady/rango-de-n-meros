numero = int(input("Ingresa un número para determinar el rango: "))
match numero: 
    case numero if numero <= 0:
        print("Es un numero negativo")
    case numero if 1 <= numero <= 10:
        print("El número está en el rango del 1 al 10")
    case numero if 11 <= numero <= 20:
        print("El número está en el rango del 11 al 20")
    case numero if 21 <= numero <= 30:
        print("El número está en el rango del 21 al 30")
    case numero if 31 <= numero <= 40:
        print("El número está en el rango del 31 al 40")
    case numero if 41 <= numero <= 50:
        print("El número está en el rango del 41 al 50")
    case numero if 51 <= numero <= 60:
        print("El número está en el rango del 51 al 60")
    case numero if 61 <= numero <= 70:
        print("El número está en el rango del 61 al 70")
    case numero if 71 <= numero <= 80:
        print("El número está en el rango del 71 al 80")
    case numero if 81 <= numero <= 90:
        print("El número está en el rango del 81 al 90")
    case numero if 91 <= numero <= 100:
        print("El número está en el rango del 91 al 100")
    case _:
        print("Error al reconocer el número")