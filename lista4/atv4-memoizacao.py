def sequencia(n, memo={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    resultado = sequencia(n-1) + 2*sequencia(n-2, memo)
    memo[n] = resultado
    return resultado

seq = lambda n:sequencia(n)

n = int(input("Entre com um número: "))
print(f"O termo T{n} da sequência é {sequencia(n)}")