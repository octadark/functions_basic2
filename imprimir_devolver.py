"""
Imprimir y devolver: crea una función que reciba una lista con dos números. 

Imprime el primer valor y devuelve el segundo.

Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2
"""
def imprimirdevolver(lista):
    print(lista[0])
    return lista[1]
    
valor_devuelto = imprimirdevolver([10,20])
print(valor_devuelto)