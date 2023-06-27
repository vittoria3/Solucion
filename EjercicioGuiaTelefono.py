lista_telefonos = [{'nombre': 'Pepito', 'telefono': 98510214}, {'nombre': 'Panchito VII', 'telefono': 72840124}, {'nombre': 'Claudia VIII', 'telefono': 75820951}, {'nombre': 'Carlos', 'telefono': 17390121}, {'nombre': 'Michi', 'telefono': 88118811}, {'nombre': 'NotMichi', 'telefono': 11881188}, {'nombre': 'Un perrito', 'telefono': 571924012}, {'nombre': 'Algun tipo que no conozco', 'telefono': 27295012}, {'nombre': 'Jerardo con J', 'telefono': 1279501023}, {'nombre': 'Gustavo', 'telefono': 1982981}, {'nombre': 'Pancha', 'telefono': 12389829}, {'nombre': 'Antonnnnnia', 'telefono': 519391241}, {'nombre': 'Gerardo sin J', 'telefono': 28495012}, {'nombre': 'Tatatatat', 'telefono': 12884192412}, {'nombre': 'Panchin', 'telefono': 12315231}]

def busqueda(cadena):
    resultado = [] #ALMACENA LOS NOMBRES Y NUMEROS ENCONTRADOS
    cadena = cadena.lower() #ALMACENA EL INPUT DEL USUARIO Y LO NORMALIZA CONVIRTIENDO TODOS SUS VALORES A MINUSCULAS
    indexador = 0 #ALMACENA EL INDICE DEL ELEMENTO QUE SE ESTA ITERANDO
    indice = []
    
    for diccionario in lista_telefonos: #ITERA CADA VALOR DE lista_telefonos Y ALMACENA EN LA VARIABLE diccionario EL VALOR QUE SE ESTA ITERANDO
        nombre = diccionario['nombre'].lower() #CREA UNA VARIABLE nombre DONDE ALMACENA EL VALOR DE LA LLAVE 'nombre' CONTENIDA EN EL VALOR QUE SE ESTA ITERANDO ACTUALMENTE (diccionario)
        telefono = str(diccionario['telefono']) #LO MISMO QUE LA LINEA ANTERIOR PERO CON LA LLAVE 'telefono' , SE DEFINE COMO str PARA PODER COMPARARLA CON LA cadena QUE INGRESA EL USUARIO Y ASI FILTRAR LOS TELEFONOS TAMBIEN
    
        if cadena in nombre or cadena in telefono: #CONDICIONAL, ESTABLECE QUE SI EL VALOR DE cadena SE ENCUNETRA DENTRO DE LA VARIABLE nombre O SI EL VALOR DE cadena SE ENCUENTRA EN telefono SE CUMPLE LA CONDICION
            resultado.append((nombre , telefono)) #AGREGA A LA LISTA DE RESULTADOS EL NOMBRE Y EL TELEFONO FILTRADO
            indice.append(indexador) #AGREGA EL VALOR ACTUAL DEL INDEXADOR A LA LISTA PARA IDENTIFICAR A CADA BUSQUEDA
        indexador = indexador + 1 #AUMENTA EL INDEXADOR EN 1, PARA QUE COINCIDA CON EL SIGUIIENTE ELEMENTO DE LA LISTA
    
    return resultado , indice

cadena = input("Ingrese su búsqueda:\n") #INPUT, PERMITE AL USUARIO INGRESAR LA CADENA DE BUSQUEDA
resultado , indice = busqueda(cadena) #TUPLA, ASIGNA EN LAS VARIABLES resultado E indice LOS RESPECTIVOS VALORES QUE RETORNA LA FUNCION busqueda(cadena)
contador = 0 #CONTADOR PARA ASIGNAR UN IDENTIFICADOR A CADA ELEMENTO DE LA LISTA resultado

for elemento in resultado: #ITERO SOBRE LOS ELEMENTOS DE resultado
    print(f"{contador}: {elemento}") #IMPRIMO EL CONTADOR Y EL elemento QUE SE ESTA ITERANDO EN CADA CICLO, DE ESTA MANERA GENERO UNA LISTA ORDENADA CON LOS VALORES DE LA LISTA resultado
    contador = contador + 1 #AUMENTO EN 1 EL VALOR DEL CONTADOR PARA QUE SE IMPRIMAN EN ORDEN AUTOMATICAMENTE PARTIENDO DESDE EL 0 PARA PODER IDENTIFICARLOS POR EL indice

decide = int(input("Desea agregar un e-mail?\n1:SI\n2:NO\n"))

if decide == 1:
    indiceCorreo = int(input("Seleccione el contacto (0/1/2/3...etc)\n")) #PIDE AL USUARIO ELEGIR EL CONTACTO AL QUE QUIERE AGREGAR EL CORREO
    correo = input("Ingrese el correo correspondiente:\n") #PIDE AL USUARIO INGRESAR EL CORREO
    lista_telefonos[indice[indiceCorreo]]['e-mail'] = correo #AGREGA EL CORREO AL CONTACTO CORRESPONDIENTE USANDO LA VARIABLE indice Y USANDO LA ELECCION DEL USUARIO PARA ENCONTRAR EL CONTACTO
    print(lista_telefonos[indice[indiceCorreo]]) #IMPRIME EL CONTACTO CON EL CORREO MODIFICADO

if decide == 2:
    print("Hasta pronto.")