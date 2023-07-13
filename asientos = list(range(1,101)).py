asientos = list(range(1,101))

def mostrar_asientos():
    contador = 1
    for i in asientos:
        print(f'{i:4}',end=' ')
        if contador % 10 == 0:
            print('')
        contador += 1

mostrar_asientos()

def menu():
    print("""
1. Comprar entrada
          2. Mostrar lista
          3.Salir
          """)
opcion = -1
while opcion != 5:
     menu()
     cont = 1
     opcion = int(input('Ingrese la opcion a realizar: \n'))
     if opcion == 1:
         entrada = int(input('Ingrese la cantidad de entradas a comprar:\n'))
         while cont <= entrada:
             cont += 1
             ubicacion = int(input('Ingrese la ubicacion que desea comprar: \n'))
             ubicacion -= 1

             if asientos[ubicacion] != '    X':
                 asientos[ubicacion] = '   X'

     if opcion == 2: 
         mostrar_asientos( )            

                 
             

    
    

