'''
    crear variable que contenga un texto y mostrar el tipo de la variable,
    crear otra variable que almacene la longitud de la variable anterior,
    crear otra variable que almacene la primera variable pero en mayusculas.
    crear otra variable que concatene la variable mayusculas y la variable de longitud

    (+5)
    '''
    
nombre = str(input("Digite su nombre: "))
longitud = len(nombre)
mayusculas = nombre.upper()
contatenacion = str(mayusculas) + str(longitud)

print(type(nombre))
print(mayusculas, longitud)
