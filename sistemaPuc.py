#Kailane Bonfati de Camargo

opcao = 1
flagStop1 = 9
while opcao != flagStop1:

    print('----- MENU PRINCIPAL -----\n')
    print('(1) Gerenciar estudantes.')
    print('(2) Gerenciar professores.')
    print('(3) Gerenciar disciplinas.')
    print('(4) Gerenciar turmas.')
    print('(5) Gerenciar matrículas.')
    print('(9) Sair.\n')
    opcao = int(input('Informe a opção desejada: '))

    gerenciamento = ""
    if opcao == 1:
        gerenciamento = "ESTUDANTES"
    elif opcao == 2:
        gerenciamento = "PROFESSORES"
        print("EM DESENVOLVIMENTO")
        input("Pressione ENTER para continuar.")
        continue
    elif opcao == 3:
        gerenciamento = "DISCIPLINAS"
        print("EM DESENVOLVIMENTO")
        input("Pressione ENTER para continuar.")
        continue
    elif opcao == 4:
        gerenciamento = "TURMAS"
        print("EM DESENVOLVIMENTO")
        input("Pressione ENTER para continuar.")
        continue
    elif opcao == 5:
        gerenciamento = "MATRICULAS"
        print("EM DESENVOLVIMENTO")
        input("Pressione ENTER para continuar.")
        continue
    elif opcao == 9:
        break
    else:
        print("\n\nOpção incorreta!")
        input("Pressione ENTER para continuar.")
        continue

    escolha = 1
    flagStop2 = 9
    listNome = []

    while escolha != flagStop2:

        print("\n\n***** ["+gerenciamento+"] MENU DE OPERAÇÕES *****\n")
        print('(1) Incluir.')
        print('(2) Listar.')
        print('(3) Atualizar.')
        print('(4) Excluir.')
        print('(9) Voltar ao menu principal.\n')
        escolha = int(input('Informe a ação desejada: '))

        if escolha == 1:
            print("\n\n===== INCLUSÃO =====\n")
            for insercao in range(1):
                codigo = int(input("Digite o codigo do estudante a ser incluido: "))
                nome = input("Digite o nome a ser incluido: ")
                cpf = input("Digite o cpf do estudante a ser incluido: ")
                aux = {
                    'codigo': codigo,
                    'nome': nome,
                    'cpf': cpf
                }
                listNome.append(aux)
                input("Pressione ENTER para continuar.")
                continue
        elif escolha == 2:
            print("\n\n===== LISTAGEM =====\n")
            if not listNome:
                print("Não há estudantes cadastrados")
                input("Pressione ENTER para continuar.")
                continue
            else:
                for nome in listNome:
                    print("* {} - {} - {} ".format(nome['codigo'], nome['nome'], nome['cpf']))
                input("Pressione ENTER para continuar.")
                continue
        elif escolha == 3:
            print("\n\n===== ATUALIZAÇÃO =====\n")

            codigoBusca = int(input("Qual seria o codigo do estudante que quer editar? \n"))
            flagVerifica = False
            for item in listNome:
                if item['codigo'] == codigoBusca:
                    print("Aluno encontrado!\nInforme os novos dados a serem atualizados: \n")
                    codigo = int(input("Digite o codigo do estudante: "))
                    nome = input("Digite o nome a ser atualizado: ")
                    cpf = input("Digite o cpf do estudante a ser atualizado: ")

                    item['codigo'] = codigo
                    item['nome'] = nome
                    item['cpf'] = cpf
                    
                    flagVerifica = True
                    break
            if not flagVerifica:
                print("Codigo não localizado")
            
            input("Pressione ENTER para continuar.")
            continue
        elif escolha == 4:
            print("\n\n===== EXCLUSÃO =====\n")
            codigoBusca = int(input("Qual seria o codigo do estudante que deseja excluir? \n"))
            flagVerifica = False
            for item in listNome:
                if item['codigo'] == codigoBusca:
                    print("Aluno encontrado!\nExcluindo Aluno... \n")
                    listNome.remove(item)
                    flagVerifica = True
                    break
            if not flagVerifica:
                print("Codigo não localizado")
            input("Pressione ENTER para continuar.")
            continue
        elif escolha == 9:
            continue
        else:
            print("\n\nOpção incorreta!")
            input("Pressione ENTER para continuar.")
            continue


print("Finalizando aplicação...")
