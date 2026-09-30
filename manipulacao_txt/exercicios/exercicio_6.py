def carregar_nomes():
    with open("nomes.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana\n")
        arquivo.write("Bruno\n")
        arquivo.write("Carlos\n")
        arquivo.write("Daniela\n")
        arquivo.write("Eduardo\n")
        arquivo.write("Fernanda\n")
        arquivo.write("Gabriel\n")

    with open("nomes.txt", "r", encoding="utf-8") as arquivo:

        nomes_alunos = [nomes.strip() for nomes in arquivo]

        print(f"lista de alunos: {nomes_alunos}")

carregar_nomes()