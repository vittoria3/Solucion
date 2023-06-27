agenda = {
    'Nombre': 98510214,
    'Panchito VII': 72840124,
    'Claudia VIII': 75820951,
    'Carlos': 571924012,
    'Algun tipo que no conozco': 27295012,
    'Jerardo con J': 1279501023,
    'Gustavo': 1982981,
    'Pancha': 12389829,
    'Antonnnnnia': 519391241,
    'Gerardo sin J': 28495012,
    'Tatatatat': 12884192412,
    'Panchin': 12315231
}

def agregar_contacto(nombre, telefono):
    agenda[nombre] = {'telefono': telefono, 'email': None}
    print("Contacto agregado correctamente.")

def buscar_por_nombre(string):
    resultados = []
    for nombre, datos in agenda.items():
        if string.lower() in nombre.lower():
            resultados.append((nombre, datos['telefono']))
    return resultados

def buscar_por_telefono(numero):
    resultados = []
    for nombre, datos in agenda.items():
        if str(numero) == str(datos['telefono']):
            resultados.append((nombre, datos['telefono']))
    return resultados

def mostrar_resultados(resultados):
    if resultados:
        print("Resultados:")
        for nombre, telefono in resultados:
            print("Nombre: ", nombre)
            print("Teléfono: ", telefono)
            print("--------------------")
    else:
        print("No se encontraron resultados.")

def agregar_email(nombre):
    if nombre in agenda:
        opcion = input("¿Desea agregar, reemplazar o quitar el email? (agregar/reemplazar/quitar): ")
        if opcion == "agregar":
            email = input("Ingrese el email: ")
            agenda[nombre]['email'] = email
            print("Email agregado correctamente.")
        elif opcion == "reemplazar":
            email = input("Ingrese el nuevo email: ")
            agenda[nombre]['email'] = email
            print("Email reemplazado correctamente.")
        elif opcion == "quitar":
            agenda[nombre]['email'] = None
            print("Email eliminado correctamente.")
        else:
            print("Opción inválida. No se realizaron cambios.")
    else:
        print("El contacto no existe en la agenda.")

def mostrar_contactos():
    print('Lista de contactos')
    for nombre, datos in agenda.items():
        print('Nombre:', nombre)
        print('Teléfono:', datos['telefono'])
        print('--------------------')

def menu():
    print("Bienvenido a la Agenda Telefónica")
    print("1. Agregar contacto")
    print("2. Buscar por nombre")
    print("3. Buscar por número de teléfono")
    print("4. Agregar/reemplazar/quitar email")
    print("5. Mostrar los contactos")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        agregar_contacto(nombre, telefono)

    elif opcion == "2":
        string = input("Ingrese el nombre o parte del nombre a buscar: ")
        resultados = buscar_por_nombre(string)
        mostrar_resultados(resultados)

    elif opcion == "3":
        numero = input("Ingrese el número de teléfono a buscar: ")
        resultados = buscar_por_telefono(numero)
        mostrar_resultados(resultados)

    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto: ")
        agregar_email(nombre)

    elif opcion == "5":
        mostrar_contactos()

    elif opcion == "6":
        print("¡Hasta luego!")
        return

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

    print("\n")
    menu()

menu()