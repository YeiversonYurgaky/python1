import math

"""
x = float(input("digite x: "))

if x > 0:
    sumatoria = 0

    for n in range(10):
        logn = 2 * (1 / (2*n+1)) * ((x-1) / (x+1) ** (2*n+1))
        sumatoria = sumatoria + logn
    print(sumatoria)
    print(math.log(x))

"""
x = float(input("digite x: "))



if x > 0:
    sumatoria = 0

    for n in range(10):
        logn = 2 * (1 / (2*n+1)) * ((x-1) / (x+1) ** (2*n+1))
        sumatoria = sumatoria + logn

    log_deci = sumatoria / 2.30259
    pyth = math.log(x) / 2.30259
    print(log_deci)
    print(pyth)
 
math.tan
