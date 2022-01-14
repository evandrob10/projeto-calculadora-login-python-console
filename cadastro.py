import banco_dados
from login import logar

def register():

    new_users = input("Digite o login desejado: ")

    while new_users in banco_dados.db_users:
        if new_users:
            opt = input("Usuario ja existe! Deseja ir para o login? \n 1 - Sim \n 2 - Não \n")
            if opt == "1":
                print(logar())
            elif opt == "2":
                new_users = input("Digite o login desejado: ")
            else:
                print("Opção invalida! tente novamente...")

    new_senha = input("Digite a senha desejada: ")

    confirm_new_senha = input("Digite novamente a senha deseja: ")

    while new_senha != confirm_new_senha:
        print("As senhas não são iguais! por favor digite novamente.")
        new_senha = input("Digite a senha desejada: ")
        confirm_new_senha = input("Digite novamente a senha deseja: ")
    while new_senha == "":
        print("Você esqueceu de preencher a senha! por favor digite novamente.")
        new_senha = input("Digite a senha desejada: ")
        confirm_new_senha = input("Digite novamente a senha deseja: ")    
    while confirm_new_senha == "":
        print("Você esqueceu de preencher a senha! por favor digite novamente.")
        new_senha = input("Digite a senha desejada: ")
        confirm_new_senha = input("Digite novamente a senha deseja: ")  

    banco_dados.db_users.append(new_users)
    banco_dados.db_senha.append(new_senha)

    print(logar())
    
register()

