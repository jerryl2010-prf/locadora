from time import sleep

def cadastrar_cliente(clientes):
    sleep(0.5)
    print("--- Cadastro ---")
    sleep(0.5)
    nome = input("Digite o seu nome: ")
    sleep(0.5)
    numero = input("Digite um número de telefone: ")
    if len(clientes) > 0:
        for cliente in clientes:
            if cliente["numero"] == numero:
                sleep(0.5)
                print("Cadastro não realizado, número de telefone já utilizado!")
                sleep(0.5)
                return 
    sleep(0.5)
    senha = input("Digite uma senha: ")
    sleep(0.5)
    conf_senha = input("Confirme a senha: ")
    if senha != conf_senha:
        sleep(0.7)
        print("Não foi possível realizar o cadastro!")
        return
    cliente = {"nome": nome, "numero": numero, "senha": senha}
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")
    sleep(1)

def listar_clientes(clientes):
    contador = 0
    sleep(0.5)
    if len(clientes) == 0:
        print("Não há clientes cadastrados!")
    print("--- Catálogo de clientes ---")
    for cliente in clientes:
        contador+=1
        sleep(0.5)
        print(f"\nCliente {contador}:")
        sleep(0.5)
        print(f"Nome: {cliente["nome"]}   |   Número de telefone: {cliente["numero"]}   |   Senha: {cliente["senha"]}\n\n")
        sleep(3)