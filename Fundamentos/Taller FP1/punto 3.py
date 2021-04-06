#Yeiverson Yurgaky Jimenez

print("Punto en el plano cartesiano")

x = float(input("Digite el valor en X: "))
y = float(input("Digite el valor en Y: "))

if x > 0 and y > 0:
    print("Este punto se haya en el eje x en",x,"y en el eje y se haya en",y,". Y se encuentran en el cuadrante #1 del plano cartesiano.")

elif x > 0 and y < 0:
    print("Este punto se haya en el eje x en",x,"y en el eje -y se haya en",y,". Y se encuentran en el cuadrante #4 del plano cartesiano.")

elif x < 0 and y > 0:
    print("Este punto se haya en el eje -x en",x,"y en el eje y se haya en",y,". Y se encuentran en el cuadrante #2 del plano cartesiano.")

elif x < 0 and y < 0:
    print("Este punto se haya en el eje -x en",x,"y en el eje -y se haya en",y,". Y se encuentran en el cuadrante #3 del plano cartesiano.")

elif x == 0 and y > 0:
    print("Este punto se haya en el origen en",x,"y en el eje y se haya en",y,". Y se encuentran en el cuadrante #1 del plano cartesiano.")

elif x == 0 and y < 0:
    print("Este punto se haya en el origen en",x,"y en el eje -y se haya en",y,". Y se encuentran en el cuadrante #1 del plano cartesiano.")