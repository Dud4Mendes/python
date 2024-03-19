import random
def jogar_jokennpoo():
    opcoes = ["pedra", "papel", "tesoura"]
    vitoria = 0
    print("bem-vindo ao jogo de jokenpo")
    print("escolha entre : pedra, papel ou tesoura.")

    while True:
        escolha_jogador = input("faça sua escolha").lower()
        if escolha_jogador not in opcoes:
            print("escolha invalida, tente novamente")
            continue

        escolha_computador = random.choice(opcoes)

        print(f"computador escolheu: {escolha_computador}")    

        resultado = define_vencedor(escolha_jogador, escolha_computador)
        print(resultado)

        if resultado == "vc ganhou":
            vitoria += 1
        elif resultado == "vc perdeu":
            vitoria -= 1    
        else:
            vitoria += 0    

        print(f"seu numero de vitorias foi: {vitoria}")    

        jogar_novamente = input("vc quer jogar novamente?").lower()
        if jogar_novamente != "sim":
            break

def define_vencedor(escolha_jogador, escolha_computador):
        if escolha_jogador == escolha_computador:
            return "empate"
        elif(
            (escolha_jogador == "papel" and escolha_computador == "pedra") or 
            (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
            (escolha_jogador == "tesoura" and escolha_computador == "papel") 
            ):
            return "vc ganhou"
        else:
            return "vc perdeu"


if __name__ == "__main__":
    jogar_jokennpoo()
