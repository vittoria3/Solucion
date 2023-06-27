"""Ejercicio 1
Cree un programa que reciba "mascotas" por parte del usuario,
este ingresa el nombre y la edad
Si ingresa nombre = salir, se detiene el ingreso
Luego, imprima todos los nombres
"""
mascotas={} 

while True:
    nombre = str(input("ingrese el nombre se su mascota: "))
    if nombre == "salir":
        break
    edad = int(input("ingrese la edad de la mascota:" ))

    mascotas[nombre] = edad

    print(mascotas.keys())
