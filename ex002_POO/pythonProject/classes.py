def escolha_jogo(jogador):
    print("Escolha uma opção:")
    print("0 - Pedra")
    print("1 - Papel")
    print("2 - Tesoura")

    escolha = input(f"{jogador}, por favor, escolha 0, 1 ou 2: ")
    while escolha not in ["0", "1", "2"]:
        print("Escolha inválida. Tente novamente.")
        escolha = input(f"{jogador}, por favor, escolha 0, 1 ou 2: ")

    escolhas = {"0": "pedra", "1": "papel", "2": "tesoura"}
    return escolhas[escolha]


def vencedor(escolha1, escolha2):
    if escolha1 == escolha2:
        return "Empate!"
    elif (escolha1 == "pedra" and escolha2 == "tesoura") or \
            (escolha1 == "tesoura" and escolha2 == "papel") or \
            (escolha1 == "papel" and escolha2 == "pedra"):
        return "Jogador 1 vence!"
    else:
        return "Jogador 2 vence!"


def jogar():
    print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
    jogador1 = "Jogador 1"
    jogador2 = "Jogador 2"

    escolha1 = escolha_jogo(jogador1)
    escolha2 = escolha_jogo(jogador2)

    print(f"{jogador1} escolheu: {escolha1}")
    print(f"{jogador2} escolheu: {escolha2}")

    resultado = vencedor(escolha1, escolha2)
    print(resultado)


jogar()