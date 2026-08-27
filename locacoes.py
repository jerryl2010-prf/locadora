from time import sleep
from jogos import listar_jogos
from persistencia import gravacao_jogos

def realizar_locacao(locacoes, jogos):
    sleep(0.5)
    print("--- Locação ---")
    sleep(0.5)
    if jogos == []:
        print("Não há jogos disponiveís no catálogo!")
        sleep(0.5)
        return
    else:
        listar_jogos(jogos)
    nome = input("Digite o nome do jogo que deseja alugar: ")
    sleep(0.5)
    for jogo in jogos:
        if jogo["nome"] == nome and jogo["copias"] > 0:
            sleep(0.5)
            print(f"Jogo encontrado e disponível! Valor da diária: R${jogo["valor"]}")
            sleep(0.5)
            dias = int(input("Quantos dias deseja alugar o jogo: "))
            sleep(0.5)

            if dias < 4:
                valor_total = dias*jogo["valor"]
            elif dias > 3 and dias < 8:
                valor_total = dias*jogo["valor"] - (dias*jogo["valor"]*0.05)
            elif dias > 7:
                valor_total = dias*jogo["valor"] - (dias*jogo["valor"]*0.1)
            else:
                print("Quantidade inválida de dias!")
                sleep(0.5)
                return
            
            print(f"Valor total do jogo: R${valor_total}")
            locacao = {"jogo": nome, "dias_alocados": dias, "valor": valor_total}
            locacoes.append(locacao)
            sleep(0.5)
            print("Locação feita com sucesso!")
            jogo["copias"] = jogo["copias"] - 1
            gravacao_jogos(jogos)
            return
    print(f"Jogo não encontrado!")
    sleep(0.7)

def listar_locacoes(locacoes):
    contador = 0
    sleep(0.5)
    if len(locacoes) == 0:
        print("Não há locações cadastradas!")
        return
    print("--- Catálogo de locações ---")
    for locacao in locacoes:
        contador+=1
        sleep(0.5)
        print(f"\nCliente {contador}:")
        sleep(0.5)
        print(f"Jogo: {locacao["jogo"]}   |   Dias alocados: {locacao["dias_alocados"]}   |   Valor total: R${locacao["valor"]}\n\n")
        sleep(3)