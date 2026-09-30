def ler_arquivos():
    with open("mensagem.txt", "w") as arquivo:
        arquivo.write("Olá mundo!!\n")
        arquivo.write("Estou aprendendo Python.\n")
        arquivo.write ("Estou estudando manipulação de arquivos \n")

    with open("mensagem.txt", 'r') as arquivo:
        conteudo = arquivo.read()
        print( conteudo)


ler_arquivos()