def adicionar_frase():
    frases = input("Digite uma frase: ")
    with open("frases.txt", 'a', encoding= "UTF-8" ) as arquivo:

        arquivo.write(f"{frases}\n")

adicionar_frase()