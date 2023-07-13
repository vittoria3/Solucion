
#************************
#**********MENU**********
#************************

def mostrar_menu ():
    print("""
        **********MENU**********
        1. comprar entradas
        2. mostrar ubicacones disponibles
        3. ver listado de asistentes
        4. mostrar ganancias totales
        5. salir
""")
    

mostrar_menu()
opcion = input("selecione una opcion: ")

#************************
#*****COMPRA ENTRADA*****
#************************
if opcion == "1":
   entrada = int(input("¿Cuantas entradas desea comprar? El maximo de entradas son 3: "))
   #matriz
   lista = list(range(1,100+1))
   for i in range (0, len(lista), 10):
       sublista = lista [i:i+10]
       print(sublista)

#ubicaciones en matriz









        
elif opcion == "2":
    ubicaciones_disponibles = int(input("estas son las ubicaciones disponibles: "))
            
elif opcion == "3":
    listado_asientos = int(input("este es el listado de los que asisten: "))
            
elif opcion == "4":
    ganancias_totales = int(input("estas son las ganancias totales: "))

elif opcion == "5":
   print("saliendo del sistema: ")

else: 
   print("opcion invalida. favor de seleccionar correctamente")
        





    

