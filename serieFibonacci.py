#Este programa crea la serie de fibonacci desde 0 hasta un numero dado
def serie(num):
    lista_fibonacci = [0]
    a,b = 0,1
    for i in range(num):
        if b > num: return lista_fibonacci
        else:
            lista_fibonacci.append(b)
            a,b = b,a+b
            
print(f"La serie queda {serie(34)}")
            