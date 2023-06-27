inventario = {'Mercedez':5000,
              'Toyota':3000,
              'BMW':4500,
              'Porsche':6000,
              'Kia':3500
}

def menu():
    
    print(""" 
          1) Agrege marcas al inventario:
          
          2) Mostrar los datos del inventario:
              
          3) Filtrar por nombre de marca:
              
          4) Filtrar por precio :
              
          0) Salir
              
""")
    
def agregar_marcas(inventario):
    marca = input('Ingrese el nombre de la marca: ')
    precio = input('Ingrese el precio de la marca: ')
    inventario[marca] = precio

def mostrar_inventario(inventario):
    print('Su inventario es el siguiente: ')
    for marca,precio in inventario.items():
        print('Marca',marca)
        print('Precio',precio)
        print('- - - - - -')
        
def buscar_marca(inventario):
    filtro = input('Ingrese el nombre de la marca que busca: ')
    resultado = []
    for marca,precio in inventario.items():
       if  filtro.lower() in marca.lower():
           resultado.append((marca,precio))
           
    if resultado: 
        print('Los resultados de su busqueda son los siguientes: ')
        for marca in resultado:
         print('Marca:',marca)
    else:
        print('No existen resultados de su busqueda')         

def buscar_precio(inventario):
    precio = int(input('Ingrese el precio a buscar: '))
    resultado = []
    for marca, valor in inventario.items():
        if valor == precio:
            resultado.append((marca, valor))
            
    if resultado:
        print('Los resultados de su búsqueda son los siguientes:')
        for marca, valor in resultado:
            print('Marca:', marca)
            print('Precio:', valor)
            print('- - - - - -')
    else:
        print('No existen resultados de su búsqueda')     

def despedida():
    print('Gracias por usar nuestra aplicacion. ')
    
    
opcion = -1
   
while opcion != 0: 
    
  menu()    
  
  opcion = int(input('Ingrese la opcion del menu que desea realizar. '))
  
  if opcion == 1:
    
     agregar_marcas(inventario)
  elif opcion == 2:
     
     mostrar_inventario(inventario)
     
  elif opcion == 3:
     
    buscar_marca(inventario) 
    
  elif opcion == 4:
      
      buscar_precio(inventario)  
    
    
  elif opcion == 0:   
    
     despedida()
else:
    print('Ingresa bien el numero machucao. ')     
     