#Pra que seja reconhecido como um pacote é necessário que exista um arquivo (pode ser vazio) nomeado '__init__' dentro do pacote.

import csv

def ler_csv(path):
    with open(path, newline="", encoding='utf-8') as f
        leitor = csv.reader(f)

        dados=[]
        for linha in leitor:
            for chave, valor in linha.itens():
                linha[chave] = float(valor)



def estatisticas(dados, campo):
    valores = [linha[campo] for linha in dados]

    total = sum(valores)
    media = total/len(valores)

    return {"media ": media, "min": min(valores), "max":max(valores), "total":total}