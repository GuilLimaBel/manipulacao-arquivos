def listar_aprovados():
    alunos = []

    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;8.5\n")
        arquivo.write("Bruno;5.0\n")
        arquivo.write("Carlos;7.2\n")
        arquivo.write("Daniela;9.0\n")
        arquivo.write("Eduardo;4.5\n")
        arquivo.write("Fernanda;6.8\n")
        arquivo.write("Gabriel;5.9\n")

    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(";")
            nota = float(nota)

            alunos.append({
                "nome": nome,
                "nota": nota
            })

    print("Alunos aprovados:")

    for aluno in alunos:
        if aluno["nota"] >= 6:
            print(f'{aluno["nome"]} - {aluno["nota"]}')


listar_aprovados()