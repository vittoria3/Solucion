helados = ['Menta chips','Frutos Rojos','Selva Negra','Mora Crema','Palta Limon']
precios = [10000,5000,2000,3000,15000]
agregados = ['Chispas Chocolate','Chispas de Colores','Galleta Molida','Salsa Chocolate','Obsecion']
precios_agregados = [300,300,250,500,300]

diccionario_helados = dict(zip(helados,precios))
diccionario_agregados = dict(zip(agregados,precios_agregados))

while True:
    
    for i in range(len(helados)):
      print(i+1,helados[i],'|',precios[i],'|',i+1,agregados[i],'|',precios_agregados[i])
    
    sel = int(input('Que helado desea? '))
    sel -= 1
    
    cantidad = int(input('Cuantas Bolitas de Helado Desea Mi Dama: '))
    
    sel_agregado = int(input('Que agregado desea? '))
    sel_agregado -= 1
    
    total = cantidad * precios[sel] + precios_agregados[sel_agregado]
    
    print('El total de la compra es: ',total)
    cliente = int(input('Desea otro Helado? 1. <Si> 2. <No> '))
    
    if cliente == 1:
       continue 
   
    if cliente == 2:
        break
        
    

diccionario_helados = zip(helados,precios)
diccionario_agregados = zip(agregados,precios_agregados)