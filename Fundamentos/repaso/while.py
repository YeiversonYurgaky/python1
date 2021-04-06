"""
En un laboratorio se tiene un material de resistencia límite de 5000 ºc a temperatura ambiente de 20 ºc. 
Se introduce el material en un horno que duplica la temperatura cada 10 segundos.
Hacer algoritmo que averigüe en cuántos minutos el material se parte, es decir llegar al límite de resistencia.
"""

temperatura = 20 * 2
limite = 5000
minutos = 0

while limite > temperatura:
    minutos += 1

print(minutos)

