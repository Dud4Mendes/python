import jogo

def jogar_forca():     
    palavra_secreta = "agua"
    letras_acertadas = ["_", "_", "_", "_"]
    tentativas = 7
    while tentativas > 0 and "_" in letras_acertadas:
        palpite = input("digite uma letra").lower()
        if palpite in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if palpite == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas -= 1
        print (f"voce tem {tentativas} tentativas")
    print(" ".join(letras_acertadas))
       
    if "_" not in letras_acertadas:
        print("parabens, voce ganhou")
    else:
        print(f"voce perdeu{palavra_secreta}")
        
    jogo.escolha_jogo()

if(__name__=="__main__"):
    jogar_forca()        