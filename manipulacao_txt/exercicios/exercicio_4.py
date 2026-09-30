def contar_linhas():

    with open("nomes.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana\n")
        arquivo.write("Bruno\n")
        arquivo.write("Carlos\n")
        arquivo.write("Daniela\n")
        arquivo.write("Eduardo\n")
        arquivo.write("Fernanda\n")

    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        nomes_alunos = [nome for nome in arquivo]

    print(f" O arquivo possui {len(nomes_alunos)} linhas")
contar_linhas()
