n = int(input('Ingresa el numero de la secuencia: '))
def fib(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        
    return fib_sequence
    

result = fib(n)
print(result)




