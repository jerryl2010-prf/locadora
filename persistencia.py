import json

def gravacao_clientes(clientes):
    with open("cliente.json", "w", encoding="utf-8") as arquivo:
        json.dump(clientes, arquivo, indent=4, ensure_ascii=False)

def ler_clientes():
    try:
        with open("cliente.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
            return []

def gravacao_jogos(jogos):
     with open("jogo.json", "w", encoding="utf-8") as arquivo:
        json.dump(jogos, arquivo, indent=4, ensure_ascii=False)

def ler_jogos():
    try:
        with open("jogo.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
            return []

def gravacao_locacoes(locacoes):
    with open("locacao.json", "w", encoding="utf-8") as arquivo:
        json.dump(locacoes, arquivo, indent=4, ensure_ascii=False)

def ler_locacoes():
    try:
        with open("locacao.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
            return []