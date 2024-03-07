import forca
import adivinhacao

def escolha_jogo():
    print("************")
    print("**escolha o jogo**")
    print("************")
    print("(1)forca, (2)adivinhação")
    jogo = int(input("escolha o jogo"))
    if (jogo == 1):
        print("jogano forca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("jogando adivinhação")
        adivinhacao.jogar_adivinhacao()
if (__name__== "__main__"):
    escolha_jogo()

