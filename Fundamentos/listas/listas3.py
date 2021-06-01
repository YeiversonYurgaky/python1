"""
Se lee un vector de n elementos. Cada elemento es un bit de un número binario. A partir del número binario contenido
a lo largo del vector, obtener su equivalencia decimal.
"""
numero = []
decimal = 0
limite = int(input("Digite la cantidad de bits que tiene su número binario: "))

for i in range(0,limite):
    binario = int(input(f"Binario número {i}: "))
    numero.append(binario)
print(numero)
for i in range(limite,-1,): #for i in range(10,-1,-1):
    decimal = decimal + numero[i] * pow(2,i)

print(decimal)

"""
decimal = 0

for i in range(0,limite): #for i in range(10,-1,-1):
    decimal = decimal + numero[i] * pow(2, limite - 1 - i)
print(decimal)
"""
    