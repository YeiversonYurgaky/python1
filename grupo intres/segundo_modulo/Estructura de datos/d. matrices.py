'''
Las matrices se pueden definir de dos formas:
    Un vector bidimensional que ya no posee un solo indice sino que ahora posee subindices

    Una estructura de control que almacena datos y accede a ellos mediante filas y coljumnas

En este tipo de estructuras de datos ya no tendremos solo una posicion del array, sino que tendremos una posicion
definida por otras 2. En Python, estas se definen como listas dentro de listas... Las listas externas son las filas de
la matriz y las listas internas son las columnas de la misma. Esto puede variar segun el criterio de cada persona.

Supongamos que tenemos una matriz A

Sintaxis:
    A= [[a, b, c],[1, 2, 3],[True, False, 24.9]]

    Aquí estamos definiendo que la matriz tendrá 3 fila y  3 columnas quedando así

    [a,     b,     c]
    [1,     2,     3]
    [True, False, 24.9]



def main() :
    A= [
        ["a", "b", "c"],
        [1, 2, 3],
        [True, False, 24.9]
        ]

    B = [
        ["a", 1, True],
        ["b", 2, False],
        ["c", 3, 24.9]
        ]

    print(A [0][1])


main()

Escribir una función que reciba dos matrices y devuelva la suma.
'''

matriz1 = [[1,2],[3,4]]
matriz2 = [[1,2],[3,4]]

resultado = [[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        resultado[i][j] = matriz1[i][j] + matriz2[i][j]
print(resultado)