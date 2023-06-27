def menu():
    print("""SU AGENDA
          1) Agregar un contacto:
           
          2) Mostrar datos del contacto:
           
          3) Salir.""")

opcion = -1
agenda = []
agenda_telefonica = []

agenda_diccionario = dict(zip(agenda,agenda_telefonica))

def agregar_contacto():
    nombre = input('Ingrese el nombre del contacto: ')
    telefono = input('Ingrese el numero de telefono del contacto: ')
    agenda.append([nombre])
    agenda_telefonica.append([telefono])
    print('Se ha agregado el contacto. ')
    
def mostrar_contacto():
 
 for contacto in agenda:
     print('Datos del contacto: ',contacto)  

def despedir():
   print('Gracias hasta pronto.') 
    

while opcion != 3:
    
    menu()
    
    opcion = int(input('Ingrese la opcion que desea realizar.'))
    
    if opcion == 1:
        
        agregar_contacto()  
    
    if opcion == 2:
        
        agenda_diccionario = dict(zip(agenda,agenda_telefonica))
        print(agenda_telefonica)
        
    if opcion == 3:
        
        despedir()  
        break       