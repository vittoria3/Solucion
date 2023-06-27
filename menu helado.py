sabores = ["menta chips", "chocolate", "mora crema", "piña", "misterioso", "palta limon"]
precio = [10000, 5000, 7000, 3000, 4000, 15000]
total = 0
ganancias = 0
while(True):
    for i in range(len(sabores)):
        print(i+1, sabores[i], "$",precio[i])
    
    eleccion = int(input("eliga sabor: "))
    eleccion = eleccion - 1
    print("usted ha elegido: ", sabores[eleccion])
    total = total + precio[eleccion]
       

    extra = str(input("desea otro helado? s/n: "))
    extra_correcto = extra.lower()
    if extra_correcto == "s":
        continue

    if extra_correcto == "n":
        print("el total a pagar de: ", total)
        


    cliente = str(input("hay algun otro cliente? s/n: "))
    cliente_correcto = cliente.lower()
    if cliente_correcto == "s":
        ganancias = ganancias + total
        total = 0
        continue

    if cliente_correcto == "n":
        ganancias = ganancias + total
        print("las ganancias del dia son: ", ganancias)
    break



