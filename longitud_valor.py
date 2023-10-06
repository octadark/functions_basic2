"""
Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, 
y cuyos valores sean todos el valor dado.

Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]
"""
def tamaño_longitud(lista):
    lista_nueva = []
    cont = 1
    while cont <= lista[0]:
        lista_nueva.append(lista[1])
        cont += 1
    return lista_nueva
print(tamaño_longitud([4,7]))
print(tamaño_longitud([6,2]))
#al imprimir