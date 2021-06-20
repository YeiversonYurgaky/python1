m = [[8,3,4],[1,5,9],[6,7,2]]

diagonal_p = diagonal_s = 0
listA = []
listB = []

#Diagonales
for filas in range(0,3):

    for columnas in range(0,3):
        if filas == columnas:
            diagonal_p += m[filas][columnas]
        if (filas+columnas) == 2:
            diagonal_s += m[filas][columnas]

#Sumatoria de filas

for filas in range(0,3):
    sma_filas = 0
    for columnas in range(0,3):
        sma_filas += m[filas][columnas]
    
    listA.append(sma_filas)

#Sumatorias de columnas

for columnas in range(0,3):
    sma_columnas = 0
    for filas in range(0,3):
        sma_columnas += m[filas][columnas]
    
    listB.append(sma_columnas)

print(diagonal_p)
print(diagonal_s)
print(listA[:])
print(listB[:])