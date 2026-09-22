""" Sistema de Autenticação
Solicita uma senha até o usuário acertar. Conta o número de
tentativas e bloqueia o acesso após 3 erros, usando while.
"""


def sistema_autenticacao():
    senha_correta = "1234"
    tentativas = 0
    acesso = False

    while tentativas < 3 and not acesso:
        senha = input("Digite a senha: ")
        tentativas += 1

        if senha == senha_correta:
            acesso = True
            print("Acesso concedido!")
        else:
            print(f"Senha incorreta. Tentativas restantes: {3 - tentativas}")

    if not acesso:
        print("Acesso bloqueado. Número máximo de tentativas excedido.")


if __name__ == "__main__":
    sistema_autenticacao()

"""
Portugol 

programa
{
    funcao inicio()
    {
        cadeia senha
        cadeia senhaCorreta = "1234"
        inteiro tentativas = 0
        logico acesso = falso

        enquanto (tentativas < 3 e !acesso)
        {
            escreva("Digite a senha: ")
            leia(senha)
            tentativas = tentativas + 1

            se (senha == senhaCorreta)
            {
                acesso = verdadeiro
                escreva("Acesso concedido!")
            }
            senao
            {
                escreva("Senha incorreta. Tentativas restantes: ", 3 - tentativas)
            }
        }

        se (!acesso)
        {
            escreva("Acesso bloqueado. Número máximo de tentativas excedido.")
        }
    }
}
"""