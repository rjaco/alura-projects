
def jogar():

    print("*******************************")
    print("**Bem vindo ao jogo de Forca!**")
    print("*******************************")

    palavra_secreta = "banana".upper()
    enforcou = False
    acertou  = False    
    
    while (not enforcou and not acertou):
        
        
        chute = input("Digite uma letra: ").strip() 
               
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                #print(f"Encontrei a letra {letra} na posição {index}")   
                print("Encontrei a letra {} na posição {}".format(letra, index))         
            index = index + 1
                
        print("jogando")
    
    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
