
semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
productos = ["catchow", "dogchow", "casuariochow", "jugete con catnip", "pelota de tenis para morder", "collar para tejones"]
animales = ["gatos", "perros","erizos","ornitorrincos", "jirafas", "cocodrilos", "hurones", "casuarios", "conejos", "cuyis", "liebres", "suricatas", "tejones"]
precio = [2500, 2500, 4000, 1000, 600, 12340]
stock = [4, 3, 4, 10, 10, 1]


while(True):

    for i in range(len(semana)):
        print(i+1, semana[i])
    dia = int(input("seleccione dia de la semana: "))
    
    cantidad = str(input("hay clientes para el dia de hoy? s/n: ").lower())
    if cantidad == "s":
        input("ingrese nombre cliente: ")
        for x in range(len(animales)):
            print(x+1, animales[x])
        int(input("ingrese tipo de animal: "))

        for y in range(len(productos)):
            print(y+1, productos[y])
        lia_maria = int(input("ingrese numero del producto: "))
        stock[lia_maria-1] = stock[lia_maria-1] - 1


        print("")
        print("======== Lista productos ========")
        for l in range(len(productos)):
            print(l+1, productos[l],"$" ,precio[l], "el stock es de: " ,stock[l] )

        print("")
        cantidad = str(input("hay mas clientes para el dia de hoy? s/n: ").lower())
        
        while cantidad == "s":
            input("ingrese nombre cliente: ")
            for z in range(len(animales)):
                print(z+1, animales[z])
            int(input("ingrese tipo de animal: "))

            for y in range(len(productos)):
                print(y+1, productos[y])
            lia_maria = int(input("ingrese numero del producto: "))
            stock[lia_maria-1] = stock[lia_maria-1] - 1

            print("")
            print("======== Lista productos ========")
            for l in range(len(productos)):
                print(l+1, productos[l],"$" ,precio[l], "el stock es de: " ,stock[l] )

            print("")
            cantidad = str(input("hay mas clientes para el dia de hoy? s/n: ").lower())
    continue                

        
            



    break
















""" x = int(input("digite producto: "))
x = int(x)
print("El nombre del producto es: ", nombre[x])
print("El precio del producto es: ", precio[x])
print("La cantidad del producto es: ", cantidad[x]) """