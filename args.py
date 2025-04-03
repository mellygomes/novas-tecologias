# '*' utilizada para listas

def soma(*args): 
    s = 0
    for i in args:
        s+=i

    return s

print(soma(1, 2, 3, 4))

# '**kwargs' indica que a funcao espera um dicionário

def calculadora( **kwargs):
    for chave, valores in kwargs.items():
        match chave:
            case '+':
                som = 0
                for valor in valores:
                    soma += valor
            case '-':
                sub = 0
                for valor in valores:
                    soma -= valor 
            
            case '*':
                mult = 1
                for valor in valores:
                    soma *= valor 

            case '/':
                div = 1
                for valor in valores:
                    soma /= valor 
    
    return som, sub, mult, div

dict = {'+': [1, 2, 3], '-': [10, 2, 3], '*': [3, 4, 9], '/': [10, 2, 3]}

som, sub, mult, div = calculadora(**dict)