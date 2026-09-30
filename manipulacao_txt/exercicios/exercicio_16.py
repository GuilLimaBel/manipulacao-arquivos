def buscar_produto():
    produtos = []

    with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(";")

            produto = {
                "nome": nome,
                "preco": float(preco),
                "quantidade": int(quantidade)
            }

            produtos.append(produto)

    nome_pesquisa = input("Digite o produto: ")
    encontrado = False

    for produto in produtos:
        if produto["nome"].lower() == nome_pesquisa.lower():
            print("Produto encontrado!")
            print("Nome:", produto["nome"])
            print("Preço: R$", format(produto["preco"], ".2f"))
            print("Quantidade:", produto["quantidade"])
            encontrado = True

    if encontrado == False:
        print("Produto não encontrado!")

buscar_produto()
