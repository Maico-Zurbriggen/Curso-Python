#En este programa haremos una función que nos devuelva los numeros primos desde el 0 hasta un valor que le pasemos
def buscando_primos(tope):
    primos = []
    for i in range(1,tope+1):
        primos.append(i) #Agregamos el numero a la lista
        for j in range(1, i):
            if i % j == 0 and j != 1:
                primos.pop(-1) #Si el numero agregado no es primo lo sacamos
                break #Salimos del segundo for para no sacar mas de un numero
    return primos

print(buscando_primos(20))