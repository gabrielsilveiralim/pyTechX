""" Lista Segura
Função que adiciona um item a uma lista sem alterar a lista
original, utilizando cópia defensiva.
"""


def adicionar_item_seguro(lista_original, item):
    """Retorna uma NOVA lista com o item adicionado,
    sem modificar a lista_original recebida."""
    nova_lista = lista_original.copy()
    nova_lista.append(item)
    return nova_lista


if __name__ == "__main__":
    original = [1, 2, 3]
    nova = adicionar_item_seguro(original, 4)
    print("Lista original:", original)
    print("Nova lista:", nova)