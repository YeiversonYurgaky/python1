#altura = float(input("Digite altura inicial de la pelota: "))
#nunrebote = 0

#while altura >= 5:
#    nunrebote = nunrebote + 1
#    altura = altura * 0.9
#print(nunrebote)

#inv = float(input("Monto inicial: "))
#tasa = float(input("digite la tasa de interes mensual: "))
#meses = 0
#meta = 2* inv

#while inv < meta:
#    meses = meses + 1
#    inv = inv * (1 + (tasa/100))
#print(meses)

p1 = int(input("Digite la población de la ciudad 1: "))
t1 = float(input("Digite la tasa de la ciudad 1: "))
p2 = int(input("Digite la población de la ciudad 2: "))
t2 = float(input("Digite la tasa de la ciudad 2: "))
aini = int(input("Digite año inicial de la simulación: "))

#CAda ciclo repesenta lo que sucede en 1 año
na = 0
while p1 <= p2:
    p1 = p1 + p1 * (t1/100)
    p2 = p2 + p2 * (t2/100)
    na = na + 1

af = aini + na

print(f"el año en que la población de la c1 es mayor que la población de la c2 es {af}")


