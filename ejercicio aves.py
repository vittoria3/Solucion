preguntas = 1
#list = ["loro", "avestruces", "gallinas", "pinguinos", "canario" , "gato"]

print("ingrese tipo de ave: ")
print("0 = loro; 1 = avestruces; 2 = gallinas; 3 = pinguinos; 4 = canario")

loro = 0
avestruz = 0
gallina = 0
pinguino = 0
canario = 0

while preguntas < 8:
    tipo_ave = input(f"ingrese {preguntas}° ave: ")
    preguntas += 1

    if tipo_ave == "0":
        loro += 1

    if tipo_ave == "1":
        avestruz += 1

    if tipo_ave == "2":
        gallina += 1

    if tipo_ave == "3":
        pinguino += 1
    
    if tipo_ave == "4":
        canario += 1

    print(loro , avestruz , gallina , pinguino , canario)

    if loro > 5:
        break

    if tipo_ave == "gato":
        break


    if preguntas == 8:

        if int(gallina) > int(pinguino):
            break



        seguir= input("quiere seguir con la cuenta? s/n: ")
        if seguir == "s": 
            preguntas = 1
        else:
            preguntas = 9



print(loro , avestruz , gallina , pinguino , canario)



    

