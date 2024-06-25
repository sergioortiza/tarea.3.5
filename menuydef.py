import os
import time
cls= "cls"

def suma(a,b):
    sumar= a+b
    print(f"La suma de ambos numeros es {sumar}")

def resta(a,b):
    sumar= a-b
    print(f"La resta de ambos numeros es {sumar}")

def multiplicacion(a,b):
    sumar= a*b
    print(f"La multiplicacion de ambos numeros es {sumar}")

def dividir(a,b):
    sumar= a/b
    print(f"La divicion de ambos numeros es {sumar}")


while True:
    try:
        print("1. Suma")
        print("2. Resta")
        print("3. Multipicacion")
        print("4. Divicion")
        print("5. Salir")
        op=int(input("Ingresa una opcion: "))
        time.sleep(2)
        os.system(cls)
    except ValueError:
        print("Ingrese Solo numeros de 1 al 5")
        break 
    if op > 5:
        print("Opcion fuera de rango usa numeros solo del 1 al 5")
        continue
    if op == 1:
        try:
            a=int(input("Ingrese el primer numero: "))
            b=int(input("Ingrese el segundo numero: "))
            suma(a,b)
            break
        except ValueError:
            print("Ingrese solo numeros")
    if op== 2:
        try:
            a=int(input("Ingrese el primer numero: "))
            b=int(input("Ingrese el segundo numero: "))
            resta(a,b)
            break
        except ValueError:
            print("Ingrese solo numeros porfavor")
    if op== 3:
        try:
            a=int(input("Ingrese el primer numero: "))
            b=int(input("Ingrese el segundo numero: "))
            multiplicacion(a,b)
            break
        except ValueError:
            print("Ingrese solo numeros porfavor")
    if op== 4:
        try:
            a=int(input("Ingrese el primer numero: "))
            b=int(input("Ingrese el segundo numero: "))
            dividir(a,b)
            break
        except ValueError:
            print("Ingrese solo numeros porfavor")
    if op== 5:
        print("Saliendo del programa")
        break
    

            
            
