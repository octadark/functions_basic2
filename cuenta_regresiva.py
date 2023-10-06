"""
Cuenta regresiva: crea una función que acepte un número como entrada. 
Devuelve una lista nueva que cuente de uno en uno,
desde el número (como elemento 0) hasta 0 (como último elemento). 

Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]
"""

def cuenta_regresiva(num):
    resultado = []
    for valor in range(num, -1, -1):
        resultado.append(valor)
    return resultado
print(cuenta_regresiva(5))