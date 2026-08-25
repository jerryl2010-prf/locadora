from clientes import cadastrar_cliente, listar_clientes
from jogos import cadastrar_jogo, listar_jogos
from locacoes import realizar_locacao, listar_locacoes
from time import sleep
import json

usuario_ger = "gerente"
senha_ger = "12345"

jogos = []
locacoes = []
clientes = []

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
            sleep(0.7)
        elif escolha == "N":
            print("Crie um cadastro:")
            cadastrar_cliente(clientes)
            sleep(0.7)
        elif escolha == "S":
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
            telefone = input("Digite seu telefone: ")
            for c in clientes:
                if c["nome"] == nome and c["senha"] == senha and c["numero"] == telefone:
                    while True:
                        sleep(0.7)
                        print("--- Menu Cliente ---")
                        sleep(0.7)
                        print("1) Realizar locação\n2) Listar jogos\n3) Sair")
                        sleep(0.7)
                        option = int(input("Digite a opção que deseja: "))
                        sleep(0.7)
                        if option == 1:
                            realizar_locacao(locacoes, jogos)
                            sleep(0.7)
                        elif option == 2:
                            listar_jogos(jogos)
                            sleep(0.7)
                        elif option == 3:
                            break
                        else:
                            print("Opção inválida!")
                            sleep(0.7)
            print("Cliente não encontrado! Verifique seus dados")
            sleep(0.7)

    elif opcao == 2:
        login = input("Digite o usuário: ")
        sleep(0.7)
        senha = input("Digite a senha: ")
        sleep(0.7)
        if senha == senha_ger and login == usuario_ger:
            while True:
                sleep(0.7)
                print("--- Menu Gerente ---")
                sleep(0.7)
                print("1) Listar clientes\n2) Listar jogos\n3) Listar locações\n4) Cadastrar jogo\n5) Sair")
                sleep(0.7)
                option = int(input("Digite a opção que deseja: "))
                sleep(0.7)
                if option == 1:
                    listar_clientes(clientes)
                elif option == 2:
                    listar_jogos(jogos)
                elif option == 3:
                    listar_locacoes(locacoes)
                elif option == 4:
                    cadastrar_jogo(jogos)
                elif option == 5:
                    break
                else:
                    print("Opção inválida!")
                    sleep(0.5)

    elif opcao == 3:
        print("Saindo...")
        sleep(0.7)
        break

    else:
        print("Opção inválida!")
        sleep(0.5)