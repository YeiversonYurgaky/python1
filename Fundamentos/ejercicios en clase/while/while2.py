"""

a,b = 0,1
ct = 2
print(a)
print(b)

while ct <= 19:
    nt = a+b
    print(nt)
    ct = ct + 1
    a = b
    b = nt
print("Contador de terminos", ct)
"""
"""
El cajero de un banco (persona en la caja) solo tiene billetes de $1000, $2000, $5000, $ 10000, $ 20000 y $ 50000;
su función es cambiar los cheques de los clientes usando el menor número de billetes. Suponiendo que todos los 
cheques son múltiplos de $ 1000. Hacer programa que le informe al cajero cuántos billetes de cada denominación 
debe entregar. No se sabe cuántos clientes van al cajero, así que el programa debe terminar cuando el cajero
digite 0 en el valor de cheque. Al final del día, el programa debe informar cuántos billetes de cada denominación
fueron gastados.
"""

"""
valChe = int(input("Digite el valor del cheque a cambiar: "))



TB50 = 0 #Total de billetes de 50.000

TB20 = 0 #Total de billetes de 20.000

TB10 = 0 #Total de billetes de 10.000

TB5 = 0 #Total de billetes de 5.000

TB2 = 0 #Total de billetes de 2.000

TB1 = 0 #Total de billetes de 1.000



while valChe != 0:

    b50 = valChe // 50000

    valChe = valChe % 50000 #valChe = valChe - b50*50000

    

    b20 = valChe // 20000

    valChe = valChe % 20000 #valChe = valChe - b20*20000



    b10 = valChe // 10000

    valChe = valChe % 10000 #valChe = valChe - b10*10000



    b5 = valChe // 5000

    valChe = valChe % 5000 #valChe = valChe - b5*5000



    b2 = valChe // 2000

    valChe = valChe % 2000 #valChe = valChe - b2*2000



    b1 = valChe // 1000

    valChe = valChe % 1000 #valChe = valChe - b1*1000



    print(f"Billetes de $50000: {b50}")

    print(f"Billetes de $20000: {b20}")

    print(f"Billetes de $10000: {b10}")

    print(f"Billetes de $5000: {b5}")

    print(f"Billetes de $2000: {b2}")

    print(f"Billetes de $1000: {b1}")



    TB50 = TB50 + b50

    TB20 = TB20 + b20

    TB10 = TB10 + b10

    TB5 = TB5 + b5

    TB2 = TB2 + b2

    TB1 = TB1 + b1



    valChe = int(input("Digite el nuevo valor de cheque: "))



print(f"Billetes de $50000: {TB50}")

print(f"Billetes de $20000: {TB20}")

print(f"Billetes de $10000: {TB10}")

print(f"Billetes de $5000: {TB5}")

print(f"Billetes de $2000: {TB2}")

print(f"Billetes de $1000: {TB1}")

El mismo ejercicio, pero tienen un número limitado de billetes por denominación- 10billetes pr denominación"""

valChe = int(input("Digite el valor del cheque a cambiar: "))



TB50 = 0 #Total de billetes de 50.000

TB20 = 0 #Total de billetes de 20.000

TB10 = 0 #Total de billetes de 10.000

TB5 = 0 #Total de billetes de 5.000

TB2 = 0 #Total de billetes de 2.000

TB1 = 0 #Total de billetes de 1.000



while valChe != 0:

    b50 = valChe // 50000

    valChe = valChe % 50000 #valChe = valChe - b50*50000

    

    b20 = valChe // 20000

    valChe = valChe % 20000 #valChe = valChe - b20*20000



    b10 = valChe // 10000

    valChe = valChe % 10000 #valChe = valChe - b10*10000



    b5 = valChe // 5000

    valChe = valChe % 5000 #valChe = valChe - b5*5000



    b2 = valChe // 2000

    valChe = valChe % 2000 #valChe = valChe - b2*2000



    b1 = valChe // 1000

    valChe = valChe % 1000 #valChe = valChe - b1*1000



    print(f"Billetes de $50000: {b50}")

    print(f"Billetes de $20000: {b20}")

    print(f"Billetes de $10000: {b10}")

    print(f"Billetes de $5000: {b5}")

    print(f"Billetes de $2000: {b2}")

    print(f"Billetes de $1000: {b1}")



    TB50 = TB50 + b50

    TB20 = TB20 + b20

    TB10 = TB10 + b10

    TB5 = TB5 + b5

    TB2 = TB2 + b2

    TB1 = TB1 + b1



    valChe = int(input("Digite el nuevo valor de cheque: "))