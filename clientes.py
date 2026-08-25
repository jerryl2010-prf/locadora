from time import sleep
clientes = []

def cadastrar_cliente(clientes):
    sleep(0.5)
    print("--- Cadastro ---")
    sleep(0.5)
    nome = input("Digite o seu nome: ")
    sleep(0.5)
    numero = input("Digite seu número de telefone: ")
    if clientes == []:
        clientes = []
    else:
        for cliente in clientes:
            if cliente["numero"] == numero:
                sleep(0.5)
                print("Cadastro não realizado, número de telefone já utilizado!")
                sleep(0.5)
                return 
    sleep(0.5)
    senha = input("Digite sua senha: ")
    sleep(0.5)
    cliente = {"nome": nome, "numero": numero, "senha": senha}
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")
    sleep(1)

def listar_clientes(clientes):
    contador = 0
    sleep(0.5)
    print("--- Catálogo de clientes ---")
    for cliente in clientes:
        contador+=1
        sleep(0.5)
        print(f"\nCliente {contador}:")
        sleep(0.5)
        print(f"Nome: {cliente["nome"]}   |   Número: {cliente["numero"]}   |   Senha: {cliente["senha"]}\n\n")
        sleep(3)