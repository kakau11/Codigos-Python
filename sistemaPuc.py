#Kailane Bonfati de Camargo
def menuPrincipal():
    print('----- MENU PRINCIPAL -----\n')
    print('(1) Gerenciar estudantes.')
    print('(2) Gerenciar professores.')
    print('(3) Gerenciar disciplinas.')
    print('(4) Gerenciar turmas.')
    print('(5) Gerenciar matrículas.')
    print('(9) Sair.\n')
    return int(input('Informe a opção desejada: '))
def menuOperacoes():
        print("\n\n***** ["+gerenciamento+"] MENU DE OPERAÇÕES *****\n")
        print('(1) Incluir.')
        print('(2) Listar.')
        print('(3) Atualizar.')
        print('(4) Excluir.')
        print('(9) Voltar ao menu principal.\n')
        return int(input('Informe a ação desejada: '))
def incluirEstudante():
        if opcao == 1:
            codigo = int(input("Digite o codigo do estudante a ser incluido: "))
            nome = input("Digite o nome a ser incluido: ")
            cpf = input("Digite o cpf do estudante a ser incluido: ")
            estudante = {
                'codigo': codigo,
                'nome': nome,
                'cpf': cpf
            }
            listNome.append(estudante)
        elif opcao == 2:
             codigo = int(input("Digite o codigo do professor a ser incluido: "))
             nome = input("Digite o nome a ser incluido: ")
             cpf = input("Digite o cpf do estudante a ser incluido: ")
             professor = {
                'codigo': codigo,
                'nome': nome,
                'cpf': cpf
            }
             listNome.append(professor)
def listarEstudante():
        if opcao == 1:
            while escolha == 2:
                if not listNome:
                    print(("Não há estudantes cadastrados"))
                    break
                else:
                    for nome in listNome:
                        print("* {} - {} - {} ".format(nome['codigo'], nome['nome'], nome['cpf']))
                    break
        elif opcao == 2:
             while escolha == 2:
                if not listNome:
                    print(("Não há professores cadastrados"))
                    break
                else:
                    for nome in listNome:
                        print("* {} - {} - {} ".format(nome['codigo'], nome['nome'], nome['cpf']))
                    break        
def editarEstudante():
        codigoBusca = int(input("Qual seria o codigo do estudante que quer editar? \n"))
        flagVerifica = False
        for item in listNome:
            if item['codigo'] == codigoBusca:
                print("Aluno encontrado!\nInforme os novos dados a serem atualizados: \n")
                codigo = int(input("Digite o novo codigo a ser atualizado: "))
                nome = input("Digite o novo nome a ser atualizado: ")
                cpf = input("Digite o novo cpf a ser atualizado: ")

                item['codigo'] = codigo
                item['nome'] = nome
                item['cpf'] = cpf
                
                flagVerifica = True
                break
        if not flagVerifica:
            print("Codigo não localizado")
def excluirEstudante():
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

opcao = 1
flagStop1 = 9

while opcao != flagStop1:
    opcao = menuPrincipal()

    gerenciamento = ""
    if opcao == 1:
        gerenciamento = "ESTUDANTES"
    elif opcao == 2:
        gerenciamento = "PROFESSORES"
        # print("EM DESENVOLVIMENTO")
        input("Pressione ENTER para continuar.")
        # continue
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
        
        escolha = menuOperacoes()

        if escolha == 1:
            print("\n\n===== INCLUSÃO =====\n")
            incluirEstudante()
            input("Pressione ENTER para continuar.")
            continue
        elif escolha == 2:
            print("\n\n===== LISTAGEM =====\n")
            listarEstudante()
            input("Pressione ENTER para continuar.")
            continue
        elif escolha == 3:
            print("\n\n===== ATUALIZAÇÃO =====\n")
            editarEstudante()
            input("Pressione ENTER para continuar.")
            continue
        elif escolha == 4:
            print("\n\n===== EXCLUSÃO =====\n")
            excluirEstudante()
            input("Pressione ENTER para continuar.")
            continue
        elif escolha == 9:
            continue
        else:
            print("\n\nOpção incorreta!")
            input("Pressione ENTER para continuar.")
            continue

print("Finalizando aplicação...")
