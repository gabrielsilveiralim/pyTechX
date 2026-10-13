
def cadastrar_produtos():
    produtos = []
    try:
        quantidade = int(input("Quantos produtos deseja cadastrar? "))
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
    except ValueError as erro:
        print(f"Quantidade inválida: {erro}")
        return []

    for i in range(quantidade):
        print(f"\nProduto {i + 1}")
        nome = input("Nome: ").strip()
        categoria = input("Categoria: ").strip()
        try:
            preco = float(input("Preço (R$): ").replace(",", "."))
            if preco < 0:
                raise ValueError("O preço não pode ser negativo")
        except ValueError as erro:
            print(f"Preço inválido ({erro}). Produto ignorado")
            continue

        produtos.append({"nome": nome, "preco": preco, "categoria": categoria})
    return produtos


def analisar_produtos(produtos):
    if not produtos:
        print("Nenhum produto válido cadastrado.")
        return

    limite = float(input("\nInforme o preço-limite para filtragem: ").replace(",", "."))
    criterio = input("Digite 'acima' ou 'abaixo': ").strip().lower()
    if criterio == "acima":
        filtrados = [p for p in produtos if p["preco"] > limite]
    elif criterio == "abaixo":
        filtrados = [p for p in produtos if p["preco"] < limite]
    else:
        print("Critério inválido; a filtragem foi ignorada.")
        filtrados = []

    crescente = produtos.copy()
    crescente.sort(key=lambda p: p["preco"])
    decrescente = sorted(produtos, key=lambda p: p["preco"], reverse=True)
    categorias = set(p["categoria"] for p in produtos)
    precos = [p["preco"] for p in produtos]
    estatisticas = (min(precos), max(precos), sum(precos) / len(precos))

    print("\n Relatório de produtos: ")
    print(f"Total de produtos válidos: {len(produtos)}")
    print(f"Filtro ({criterio}, R$ {limite:.2f}):")
    for p in filtrados:
        print(f"- {p['nome']} | {p['categoria']} | R$ {p['preco']:.2f}")

    print("\nPreços em ordem crescente:")
    for p in crescente:
        print(f"- {p['nome']}: R$ {p['preco']:.2f}")

    print("\nPreços em ordem decrescente:")
    for p in decrescente:
        print(f"- {p['nome']}: R$ {p['preco']:.2f}")

    print(f"\nCategorias únicas: {', '.join(sorted(categorias))}")
    print(f"Estatísticas (menor, maior, média): "
          f"(R$ {estatisticas[0]:.2f}, R$ {estatisticas[1]:.2f}, R$ {estatisticas[2]:.2f})")


if __name__ == "__main__":
    dados = cadastrar_produtos()
    analisar_produtos(dados)
