""" Análise de Números
Lê 5 números via input() e calcula a soma, a média, o maior
e o menor valor, usando a estrutura de repetição for.
"""


def analisar_numeros():
    numeros = []
    for i in range(1, 6):
        numero = float(input(f"Digite o número {i}: "))
        numeros.append(numero)

    soma = sum(numeros)
    media = soma / len(numeros)
    maior = max(numeros)
    menor = min(numeros)

    print(f"Soma: {soma}")
    print(f"Média: {media}")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")


if __name__ == "__main__":
    analisar_numeros()

"""
Portugol 

programa
{
    funcao inicio()
    {
        real numero, soma, maior, menor, media
        inteiro i

        soma = 0

        para (i = 1; i <= 5; i++)
        {
            escreva("Digite o número ", i, ": ")
            leia(numero)

            soma = soma + numero

            se (i == 1)
            {
                maior = numero
                menor = numero
            }
            senao
            {
                se (numero > maior)
                {
                    maior = numero
                }
                se (numero < menor)
                {
                    menor = numero
                }
            }
        }

        media = soma / 5

        escreva("Soma: ", soma)
        escreva("Média: ", media)
        escreva("Maior valor: ", maior)
        escreva("Menor valor: ", menor)
    }
}
"""