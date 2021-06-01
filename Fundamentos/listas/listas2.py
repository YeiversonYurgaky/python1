x = int(input("Digite el número de elementos: "))



A = []

B = []

C = []

for i in range(0,x):

    val = int(input(f"Digite el valor de la posición {i}: "))

    A.append(val)


pc = -1
pb = -1


for i in range(0,x):

    if A[i] % 2 == 0:
        pb = pb + 1
        #B.append(A[i])
        B.insert(pb, A[i])
    if A[i] % 3 == 0:
        pc = pc + 1
        #C.append(A[i])
        C.insert(pc,A[i])



print(B[:])

print(C[:])