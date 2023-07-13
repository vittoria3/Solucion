lista=list(range(1,101))

def menu ():
    print("""
    1.  compra entrada
    2.  mostrar asientos
    3.  rut
    4. ganancias totales
    5. salir
    """)
    
def mostrar_asientos ():
   contador = 1
   for i in lista:
      print(f'{i:4}',end='')
      if contador % 10 == 0:
         print('')
      contador +=1

mostrar_asientos()
        
             


selec = -1
while selec != 5:
   menu()
   
   selec = int(input('Ingrese la opcion que va a realizar: '))
   
   if selec == 1:
     print ("")
