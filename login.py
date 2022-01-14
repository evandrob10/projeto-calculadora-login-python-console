import banco_dados,time

def logar():
    opt = input("Qual das opçoes abaixo você deseja? \n 1 - Login \n 2 - Cadastro \n 3 - Sair \n")

    while opt != 3:

        if opt == "1": 

            usuario = str(input("Digite seu login: ")).lower()
            usuario = usuario.strip()
            senha = str(input("Digite sua senha: ")).lower()
            senha = senha.strip()

            while usuario not in banco_dados.db_users:
                print("Usuario invalido! tente novamente")
                usuario = input("Digite seu login: ")

            while senha not in banco_dados.db_senha:
                print("Senha invalida! tente novamente")
                senha = input("Digite novamente sua senha: ")

            import sistema 

        elif opt == "2":
            import cadastro
        elif opt == "3":
            print("Encerrando Sistema...")
            time.sleep(3)
            print("Sistema finalizado! Até a proxima!")
            exit()
        else:
            print("Opção invalida! tente novamente...")
logar()

