""" Classificador de Cliente
Recebe a idade e a renda de um cliente e o classifica em
Bronze, Prata, Ouro ou Diamante usando if / elif / else.
"""

def classificar_cliente(idade: int, renda: float) -> str:
    if idade >= 18 and renda >= 10000:
        return "Diamante"
    elif renda >= 5000:
        return "Ouro"
    elif renda >= 2000:
        return "Prata"
    else:
        return "Bronze"


def main():
    idade = int(input("Digite a idade do cliente: "))
    renda = float(input("Digite a renda do cliente: "))
    categoria = classificar_cliente(idade, renda)
    print(f"Categoria do cliente: {categoria}")

if __name__ == "__main__":
    main()

"""
Portugol

programa
{
    funcao inicio()
    {
        inteiro idade
        real renda
        cadeia categoria

        escreva("Digite a idade do cliente: ")
        leia(idade)
        escreva("Digite a renda do cliente: ")
        leia(renda)

        se (idade >= 18 e renda >= 10000)
        {
            categoria = "Diamante"
        }
        senao se (renda >= 5000)
        {
            categoria = "Ouro"
        }
        senao se (renda >= 2000)
        {
            categoria = "Prata"
        }
        senao
        {
            categoria = "Bronze"
        }

        escreva("Categoria do cliente: ", categoria)
    }
}
"""