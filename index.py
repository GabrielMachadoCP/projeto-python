print("Seja bem vindo à plataforma de descarte da Urbitável. Deseja fazer o seu cadastro?")
resposta = input()

if resposta == "não":
    print("Ok! Programa encerrado. ")
else:
    print("Digite seu novo usuario.")
    usuario = input()
    print("Ok! Agora digite sua nova senha.")
    senha = int(input())
    print("Cadastro feito. Deseja fazer o login?")
    respostaLogin = input()
    if respostaLogin == "não":
        print("Ok! Programa encerrado. ")
    else:
        print("Insira seu usuario cadastrado.")
        login = input()
        if login != usuario:
            print("Usuário incorreto. Tente novamente.")
        else:
            print("Ok! Agora digite sua senha cadastrada.")
            senhaLogin = int(input())
            if senhaLogin != senha:
                print("Senha incorreta, digite novamente.")
            else:
                print("Login feito. Seja bem vindo,", usuario,"!")
                print("O que deseja fazer em nossa plataforma?  REALIZAR SAQUE | FALE CONOSCO | SOBRE NÓS | SAIR DA MINHA CONTA")
                decisãoUsuario = input()

                #estrutura menu programa
                if decisãoUsuario == "realizar saque":
                    print("Ok! Qual seria a sua forma de realizar o saque,",usuario,"?" " >>> OPÇÕES: PIX | TRANSAÇÃO BANCÁRIA <<<")
                    formadepag = input()
                    if formadepag == "pix":
                        print("Certo! Registre sua chave PIX e faremos o depósito em até 24h após a solicitaçaõ. Ajudo em algo mais?")
                    else:
                        print("Certo! Registre suas credenciais bancárias e faremos o depósito em até 24h após a solicitaçaõ. Ajudo em algo mais?")
                    respostajuda = input()
                    if respostajuda == "sim":
                        print("O que deseja fazer em nossa plataforma?  REALIZAR SAQUE | FALE CONOSCO | SOBRE NÓS | SAIR DA MINHA CONTA")
                    elif respostajuda == "não":
                        print("Ok! Programa encerrado.")
                elif decisãoUsuario == "fale conosco":
                    print("Mande um email para o nosso suporte. O nosso email é urbitável@atendimento.com.br.")
                elif decisãoUsuario == "sobre nós":
                    print("Somos um grupo de estudantes de Engenharia de Software.")
                elif decisãoUsuario == "sair da minha conta":
                    print("Você saiu da sua conta. Até mais!")
                     








