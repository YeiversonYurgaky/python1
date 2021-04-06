#Yeiverson Yurgaky Jimenez

print("≈≈Descruba sus notas y si debe presentar o no el examen final≈≈")

seguimiento = float(input("Digite su nota de seguimiento: "))
parcial_1 = float(input("Digite su nota de su parcial n° 1: "))
parcial_2= float(input("Digite su nota de su parcial n° 2: "))

seguimiento = seguimiento*0.3
parcial_1 = parcial_1*0.2
parcial_2 = parcial_2*0.2
deff_1 = seguimiento + parcial_1 + parcial_2


if seguimiento < 0:
    print("Las notas no pueden ser negativas")

elif deff_1 >= 3.0:
    print("No debes presentar el examen final. Su nota ha sido de: ",deff_1)

elif deff_1 < 3.0 and deff_1 >=1.5:
    print("Debe presentar el final. Su nota ha sido de: ",deff_1)
    
    examen_final = float(input("Digite una nota ficticia, para saber cuando necesita sacar en el examen final para ganar la materia: "))
    if examen_final < 0:
        print("Las notas no pueden ser negativas")

    else:
            #Aquí calculamos con cual nota puede ser posible que gane la materia
        notadefinitiva = deff_1 + (examen_final*0.3)
        print("Si su nota ficticia es ",examen_final,"Su nota final seria ",notadefinitiva)

else: 
    print("Aqunque presente el examen final no podrá ganar la materia. Su nota es de: ",deff_1)






    
        

