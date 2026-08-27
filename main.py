from clientes import cadastrar_cliente, listar_clientes
from jogos import cadastrar_jogo, listar_jogos
from locacoes import realizar_locacao, listar_locacoes
from persistencia import gravacao_clientes, ler_clientes, gravacao_jogos, ler_jogos, gravacao_locacoes, ler_locacoes
from time import sleep
import json

usuario_ger = "gerente"
senha_ger = "12345"

jogos = []
jogos = ler_jogos()
locacoes = []
locacoes = ler_locacoes()
clientes = []
clientes = ler_clientes()

while True:
    print("--- Locadora ---")
    sleep(0.7)
    opcao = int(input("1) Cliente\n2) Gerente\n3) Sair\nDigite sua opção: "))
    if opcao == 1:
        escolha = input("Você tem cadastro? (S/N): ")
        if len(clientes) == 0:
            sleep(0.7)
            print("Não há cliente cadastrados")
            sleep(0.7)
            print("Crie um cadastro:")
            cadastrar_cliente(clientes)
            gravacao_clientes(clientes)
            sleep(0.7)
        elif escolha == "N":
            print("Crie um cadastro:")
            cadastrar_cliente(clientes)
            gravacao_clientes(clientes)
            sleep(0.7)
        elif escolha == "S":
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
            telefone = input("Digite seu telefone: ")
            clientes = ler_clientes()
            achou = False
            for c in clientes:
                if c["nome"] == nome and c["senha"] == senha and c["numero"] == telefone:
                    achou = True
                    sleep(0.5)
                    print(f"Bem vindo, {nome}!")
                    while True:
                        sleep(0.7)
                        print("\n--- Menu Cliente ---\n")
                        sleep(0.7)
                        print("1) Realizar locação\n2) Listar jogos\n3) Sair")
                        sleep(0.7)
                        option = int(input("Digite a opção que deseja: "))
                        sleep(0.7)
                        if option == 1:
                            realizar_locacao(locacoes, jogos)
                            sleep(0.7)
                            gravacao_locacoes(locacoes)
                        elif option == 2:
                            jogos = ler_jogos()
                            listar_jogos(jogos)
                            sleep(0.7)
                        elif option == 3:
                            break
                        else:
                            print("Opção inválida!")
                            sleep(0.7)
            sleep(0.7)
            if achou:
                pass
            else:
                print("Cliente não encontrado! Verifique seus dados")
                sleep(0.7)

    elif opcao == 2:
        login = input("Digite o usuário: ")
        sleep(0.7)
        senha = input("Digite a senha: ")
        sleep(0.7)
        if senha == senha_ger and login == usuario_ger:
            print("Bem vindo, gerente!")
            while True:
                sleep(0.7)
                print("\n--- Menu Gerente ---\n")
                sleep(0.7)
                print("1) Listar clientes\n2) Listar jogos\n3) Listar locações\n4) Cadastrar jogo\n5) Sair")
                sleep(0.7)
                option = int(input("Digite a opção que deseja: "))
                sleep(0.7)
                if option == 1:
                    clientes = ler_clientes()
                    listar_clientes(clientes)
                elif option == 2:
                    jogos = ler_jogos()
                    listar_jogos(jogos)
                elif option == 3:
                    locacoes = ler_locacoes()
                    listar_locacoes(locacoes)
                elif option == 4:
                    cadastrar_jogo(jogos)
                    gravacao_jogos(jogos)
                elif option == 5:
                    break
                else:
                    print("Opção inválida!")
                    sleep(0.5)
        else:
            sleep(0.5)
            print("Senha e/ou usuário errado(s)!")
            sleep(0.5)

    elif opcao == 3:
        print("Saindo...")
        sleep(0.7)
        break

    else:
        print("Opção inválida!")
        sleep(0.5)