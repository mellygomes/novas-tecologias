palavra = "banana"
resposta = ["_" for _ in palavra]

while True:
    palpite = input("Digite uma letra: ")

    for i, letra in enumerate(palavra):
        if palpite==letra:
            resposta[i] = letra
        else:
            print()

    for letra in resposta:
        print(letra, end="")

    if resposta == palavra:
        print("Achou a palavra!")
        break