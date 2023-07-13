def mostrar_menu ():
    print("""
        **********MENU**********
        1. comprar entradas
        2. mostrar ubicacones disponibles
        3. ver listado de asistentes
        4. mostrar ganancias totales
        5. salir
""")
        
    opcion = input("selecione una opcion: ")

    if opcion == "1":
        entrada = int(input("¿Cuantas entradas desea comprar? El maximo de entradas son 3: "))

    elif opcion == "2":
        ubicaciones_disponibles = int(input("estas son las ubicaciones disponibles: "))
        
    elif opcion == "3":
        listado_asientos = int(input("este es el listado de los que asisten: "))
        
    elif opcion == "4":
        ganancias_totales = int(input("estas son las ganancias totales: "))

    elif opcion == "5":
        print("saliendo del sistema: ")
        return
    
    else: 
        print("opcion invalida. favor de seleccionar correctamente")