from time import sleep

def cadastrar_jogo(jogos):
    sleep(0.5)
    nome = input("Digite o título do jogo que deseja cadastrar: ")
    sleep(0.5)
    plataforma = input("Digite a plataforma do jogo: ")
    sleep(0.5)
    genero = input("Digite o gênero do jogo: ")
    sleep(0.5)
    valor = float(input("Digite o valor de locação diária do jogo: R$"))
    sleep(0.5)
    copias = int(input("Digite o número de cópias totais desse jogo: "))
    sleep(0.5)
    if copias < 0:
        print("Número de cópias inválido!")
        return
    jogo = {"nome": nome, "plataforma": plataforma, "genero": genero, "valor": valor, "copias": copias}
    jogos.append(jogo)
    print("Jogo cadastrado com sucesso!")
    sleep(1)

def listar_jogos(jogos):
    contador = 0
    if len(jogos) == 0:
        print("Não há jogos cadastrados!")
        return
    sleep(0.5)
    print("--- Catálogo de jogos ---")
    for jogo in jogos:
        contador+=1
        sleep(0.5)
        print(f"\nJogo {contador}:")
        sleep(0.5)
        print(f"Título: {jogo["nome"]}   |   Plataforma: {jogo["plataforma"]}   |   Gênero: {jogo["genero"]}   |   Valor diário: R${jogo["valor"]}   |   Cópias: {jogo["copias"]}\n")
        sleep(3)