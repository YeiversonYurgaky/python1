n = int(input("Digite el número de elementos que tendrá la lista: "))

sum_mult5 = 0
lista = []

for i in range(0,n):
    ele = int(input(f"Digite el elemento de la posición {i}: "))
    lista.insert(i, ele)

for i in range(0,n):
    
    if lista[i] % 2 == 0:
        print(lista[i])

    elif lista[i] % 5 == 0:
        sum_mult5 += lista[i]

print(f"La suma de los elementos múltiplos de 5 es {sum_mult5}")