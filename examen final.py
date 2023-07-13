def menu():
    print("""
           1. Comprar entradas
           2. Mostrar ubicaciones disponibles
           3. Ver listado de asistentes
           4. Mostrar ganancias totales
           5. Salir 
           """)

def precios():
    print("""
          Platinum, $120.000. (Asientos del 1 al 20)
          Gold, $80.000. (Asientos del 21 al 50)
          Silver, $50.000. (Asientos del 51 al 100)
          """)

asientos = list(range(1,101))
lista_rut = []
precio = [120000,80000,50000]
def mostrar_asientos():
    contador = 1
    for i in asientos:
        print(f'{i:4}',end='')
     
        if contador % 10 == 0:
            print('')
        contador += 1
 
def valores():
    total = 0
    total_venta = platinum + gold + silver
    total_platinum = platinum * precio[0]
    total_gold = gold * precio[1]
    total_silver = silver * precio[2]
    total = total_platinum + total_gold + total_silver
    return total,total_platinum,total_gold,total_silver,total_venta


opcion = -1
platinum = 0
gold = 0
silver = 0
cont = 1

nombre = str(input('Ingrese su nombre y apellido '))
fecha = str(input('Ingrese la fecha de hoy en formato dd/mm/yyyy '))

while opcion != 5:
    cont = 1  
    menu()        
    opcion = int(input('Ingrese la opcion que desea realizar: '))
 
    if opcion == 1:
        rut = int(input('Ingrese su rut sin punto y sin digito verificador (Ej 18544900): '))
        rut_palabra = str(rut)
        if  len(rut_palabra) <= 8 :
            
        
            lista_rut.append(rut)
            print('La operacion a resultado exitosa')
            entrada = int(input('Ingrese la cantidad de entradas a comprar (Maximo 3): '))
            mostrar_asientos()
            precios()
            
            asiento_anterior = None
        else:
            print('Rut no cumple las caracteristicas')
            
        while cont <= entrada:
            cont += 1
            ubicacion = int(input('Ingrese la primera ubicación que desea: '))
            
            if ubicacion == asiento_anterior:
                print('El asiento ingresado es el mismo que en el bucle anterior.')
                continue
            
            asiento_anterior = ubicacion
            
            if asientos[ubicacion - 1] != '   X':
                asientos[ubicacion -1] = '   X'
            else:
                print('Asiento Ocupado')
                continue
            
            if ubicacion <= 20:
                platinum += 1
            elif 20 < ubicacion <= 50:
                gold += 1
            elif 51 < ubicacion <= 100:
                silver += 1
        
        
            
            
    elif opcion == 2:
        mostrar_asientos()
    
    elif opcion == 3:
        lista_rut.sort()
        for i in lista_rut:
            print(i)
    
    elif opcion == 4: 
        total,total_platinum,total_gold,total_silver,total_venta = valores()
        print("Platinum $120.000 |",platinum,'|',total_platinum)
        print("Gold $80.000 |",gold,'|',total_gold)
        print("Silver $50.000 |",silver,'|',total_silver)
        print('Total |',total_venta,'|',total)
    
    elif opcion == 5:
        print('Gracias por usar nuestra aplicacion',nombre,'La fecha de hoy es:',fecha)
        break