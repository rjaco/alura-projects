import forca
import adivinhacao


def escolhe_jogo():

    print("***********************")
    print("**Escolha o seu jogo!**")
    print("***********************")

    print("1 - Jogo da Forca")
    print("2 - Jogo da Adivinhação")

    jogo = int(input("Qual Jogo? "))

    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        adivinhacao.jogar()


if (__name__ == "__main__"):
    escolhe_jogo()
