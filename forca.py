import random


def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = definir_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 7
    erros = 0

    while not enforcou and not acertou:

        chute = pede_letra()

        if (chute in palavra_secreta):
            acertou_letra(chute, palavra_secreta, letras_acertadas)

        else:
            erros = errou_letra(chute, erros)
            enforcou = erros == tentativas
            if not enforcou:
                print(
                    f"Você ainda tem mais {tentativas - erros} chance", end="")
                print(f"{'s' if tentativas - erros > 1 else ''}")

        acertou = "_" not in letras_acertadas

        if not acertou and not enforcou:
            print("Segue o jogo!")

        print(letras_acertadas)

    if acertou:
        mensagem_vencedor()
    else:
        mensagem_perdeu(palavra_secreta)

    print("Fim do jogo")


def definir_palavra_secreta():

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()

    return palavra_secreta


def imprime_mensagem_abertura():
    print("*******************************")
    print("**Bem vindo ao jogo de Forca!**")
    print("*******************************")


def inicializa_letras_acertadas(palavra):

    return ["_" for letra in palavra]


def pede_letra():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute


def acertou_letra(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            #print(f"Encontrei a letra {letra} na posição {index}")
            #print("Encontrei a letra {} na posição {}".format(letra, index))
            letras_acertadas[index] = letra
        index += 1


def errou_letra(chute, erros):
    erros += 1
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    print("A palavra secreta não tem a letra {}".format(chute))
    return (erros)


def mensagem_vencedor():
    print("Parabéns! Acertou, Mizerávi!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_perdeu(palavra_secreta):
    print("Que pena! Não foi dessa vez!")
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if (__name__ == "__main__"):
    jogar()
