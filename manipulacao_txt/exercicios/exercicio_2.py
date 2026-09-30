def criar_arquivo():
    with open("frase.txt", "w") as arquivo:
        frase = input("Digite uma frase: ")
        arquivo.write(frase)

criar_arquivo()