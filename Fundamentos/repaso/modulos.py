"""
import random

valor = random.randint(0,10)
print(valor)

lista = [True,"Strings",23,False]
print(lista)

#valor aleatorio

random.shuffle(lista)
valor2 = random.choice(lista)
print(valor2)
#desordenar
random.shuffle(lista)
print(lista)
"""
"""
import  datetime
print(datetime.datetime.now())
"""
"""
import sys
import time

for i in range(100):
    time.sleep(0.5)
    sys.stdout.write("\r%d %%" % i)
    sys.stdout.