import random


def jogar():

    print("*************************************")
    print("**Bem vindo ao jogo de Adivinhação!**")
    print("*************************************")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    rodada = 1
    pontos = 10000

    # Seleção de Nível de dificuldade
    print("Selecione o nível de dificuldade:")
    print("(1) - Fácil")
    print("(2) - Médio")
    print("(3) - Difícil")

    nivel = int(input("Digite sua opção: "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    elif (nivel == 3):
        tentativas = 5

    print(numero_secreto)
    # Iteração das rodadas
    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}:".format(rodada, tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")

        print("Você digitou ", chute_str)

        chute = int(chute_str)
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        acertou = chute == numero_secreto

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        if acertou:
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            print("Errou!")
            if maior:
                print("Seu chute foi maior que o número secreto!")

            elif menor:
                print("Seu chute foi menor que o número secreto!")

            pontos_perdidos = abs(numero_secreto - chute) * \
                (tentativas - rodada) * (7 - (nivel * 2))
            pontos = pontos - pontos_perdidos

    print("O número secreto era ", numero_secreto)
    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
