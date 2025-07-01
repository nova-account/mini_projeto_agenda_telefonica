contato1 = None
contato2 = None
contato3 = None
contato4 = None
contato5 = None

while True:
    print("\n===== Menu Principal =====")
    print("1 - Inserir Contato")
    print("2 - Listar Contatos")
    print("3 - Imprimir Detalhes de um Contato")
    print("4 - Atualizar Contato")
    print("5 - Remover Contato")
    print("6 - Sair")

    comando = input("Escolha uma opção de 1 a 6: ").strip()

    if comando == "1":
        posicao = 0
        if contato1 is None:
            posicao = 1
        elif contato2 is None:
            posicao = 2
        elif contato3 is None:
            posicao = 3
        elif contato4 is None:
            posicao = 4
        elif contato5 is None:
            posicao = 5
        else:
            print("A lista de contatos está cheia.")
            continue

        primeiro_nome = input("Digite o primeiro nome (até 20 letras): ").strip()
        while not (primeiro_nome.isalpha() and len(primeiro_nome) <= 20):
            print("Nome inválido!")
            primeiro_nome = input("Digite o primeiro nome: ").strip()

        sobrenome = input("Digite o sobrenome (até 20 letras): ").strip()
        while not (sobrenome.isalpha() and len(sobrenome) <= 20):
            print("Sobrenome inválido!")
            sobrenome = input("Digite o sobrenome: ").strip()

        telefone = input("Digite o número de telefone (opcional, até 15 números). Pressione Enter para deixar em branco: ").replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        while telefone and (not telefone.isdigit() or len(telefone) > 15):
            print("Telefone inválido!")
            telefone = input("Digite o número de telefone (opcional): ").strip()

        celular = input("Digite o número de celular (obrigatório, até 15 números): ").replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        while not (celular.isdigit() and len(celular) <= 15):
            print("Celular inválido!")
            celular = input("Digite o número de celular: ").strip()

        email = input("Digite o e-mail (exemplo@dominio.com): ").strip().lower()
        while True:
            permitido_local_chars = "abcdefghijklmnopqrstuvwxyz0123456789._+-"
            permitido_domain_chars = "abcdefghijklmnopqrstuvwxyz0123456789.-"
            partes = email.split('@', 1)
            if len(partes) == 2 and partes[0] and partes[1] and '.' in partes[1]:
                local, dominio = partes
                partes_dominio = dominio.rsplit('.', 1)
                nome_dominio, tld = partes_dominio
                if (
                    all(c in permitido_local_chars for c in local) and
                    local[0] not in '._+-' and local[-1] not in '._+-' and
                    '..' not in local and '__' not in local and '++' not in local and
                    all(c in permitido_domain_chars for c in dominio) and
                    dominio[0] != '-' and nome_dominio[-1] != '-' and
                    '--' not in dominio and
                    len(tld) >= 2 and tld.isalpha()
                ):
                    break
            print("E-mail inválido!")
            email = input("Digite o e-mail novamente: ").strip().lower()

        dia = input("Digite o dia de nascimento (DD): ").strip()
        while not (dia.isdigit() and len(dia) == 2 and 1 <= int(dia) <= 31):
            print("Dia inválido!")
            dia = input("Digite o dia de nascimento (DD): ").strip()

        mes = input("Digite o mês de nascimento (MM): ").strip()
        while not (mes.isdigit() and len(mes) == 2 and 1 <= int(mes) <= 12):
            print("Mês inválido!")
            mes = input("Digite o mês de nascimento (MM): ").strip()

        ano = input("Digite o ano de nascimento (AAAA): ").strip()
        while not (ano.isdigit() and len(ano) == 4 and 1900 <= int(ano) <= 2025):
            print("Ano inválido!")
            ano = input("Digite o ano de nascimento (AAAA): ").strip()

        contato = {
            "nome": primeiro_nome,
            "sobrenome": sobrenome,
            "telefone": telefone,
            "celular": celular,
            "email": email,
            "aniversario": dia + "/" + mes + "/" + ano
        }

        if posicao == 1:
            contato1 = contato
        elif posicao == 2:
            contato2 = contato
        elif posicao == 3:
            contato3 = contato
        elif posicao == 4:
            contato4 = contato
        elif posicao == 5:
            contato5 = contato

        print("Contato inserido com sucesso.")

    elif comando == "2":
        if contato1 is None and contato2 is None and contato3 is None and contato4 is None and contato5 is None:
            print("Agenda vazia.")
        else:
            print("\n--- Lista de Contatos ---")
            if contato1:
                print("1 - " + contato1['nome'] + " " + contato1['sobrenome'])
            if contato2:
                print("2 - " + contato2['nome'] + " " + contato2['sobrenome'])
            if contato3:
                print("3 - " + contato3['nome'] + " " + contato3['sobrenome'])
            if contato4:
                print("4 - " + contato4['nome'] + " " + contato4['sobrenome'])
            if contato5:
                print("5 - " + contato5['nome'] + " " + contato5['sobrenome'])

    elif comando == "3":
        primeiro_nome = input("Digite o primeiro nome: ").strip()
        sobrenome = input("Digite o sobrenome: ").strip()
        achou = False
        if contato1 and contato1["nome"].lower() == primeiro_nome.lower() and contato1["sobrenome"].lower() == sobrenome.lower():
            print("\n--- Detalhes do Contato ---")
            print("Nome: " + contato1['nome'])
            print("Sobrenome: " + contato1['sobrenome'])
            print("Telefone: " + (contato1['telefone'] or '(vazio)'))
            print("Celular: " + contato1['celular'])
            print("E-mail: " + contato1['email'])
            print("Aniversário: " + contato1['aniversario'])
            achou = True

        elif contato2 and contato2["nome"].lower() == primeiro_nome.lower() and contato2["sobrenome"].lower() == sobrenome.lower():
            print("\n--- Detalhes do Contato ---")
            print("Nome: " + contato2['nome'])
            print("Sobrenome: " + contato2['sobrenome'])
            print("Telefone: " + (contato2['telefone'] or '(vazio)'))
            print("Celular: " + contato2['celular'])
            print("E-mail: " + contato2['email'])
            print("Aniversário: " + contato2['aniversario'])
            achou = True

        elif contato3 and contato3["nome"].lower() == primeiro_nome.lower() and contato3["sobrenome"].lower() == sobrenome.lower():
            print("\n--- Detalhes do Contato ---")
            print("Nome: " + contato3['nome'])
            print("Sobrenome: " + contato3['sobrenome'])
            print("Telefone: " + (contato3['telefone'] or '(vazio)'))
            print("Celular: " + contato3['celular'])
            print("E-mail: " + contato3['email'])
            print("Aniversário: " + contato3['aniversario'])
            achou = True

        elif contato4 and contato4["nome"].lower() == primeiro_nome.lower() and contato4["sobrenome"].lower() == sobrenome.lower():
            print("\n--- Detalhes do Contato ---")
            print("Nome: " + contato4['nome'])
            print("Sobrenome: " + contato4['sobrenome'])
            print("Telefone: " + (contato4['telefone'] or '(vazio)'))
            print("Celular: " + contato4['celular'])
            print("E-mail: " + contato4['email'])
            print("Aniversário: " + contato4['aniversario'])
            achou = True

        elif contato5 and contato5["nome"].lower() == primeiro_nome.lower() and contato5["sobrenome"].lower() == sobrenome.lower():
            print("\n--- Detalhes do Contato ---")
            print("Nome: " + contato5['nome'])
            print("Sobrenome: " + contato5['sobrenome'])
            print("Telefone: " + (contato5['telefone'] or '(vazio)'))
            print("Celular: " + contato5['celular'])
            print("E-mail: " + contato5['email'])
            print("Aniversário: " + contato5['aniversario'])
            achou = True
            
        if not achou:
            print("Contato não encontrado.")

    elif comando == "4":
        primeiro_nome = input("Digite o primeiro nome do contato a ser atualizado: ").strip()
        sobrenome = input("Digite o sobrenome do contato a ser atualizado: ").strip()

        contato_a_atualizar = None

        if contato1 and contato1["nome"].lower() == primeiro_nome.lower() and contato1["sobrenome"].lower() == sobrenome.lower():
            contato_a_atualizar = contato1
        elif contato2 and contato2["nome"].lower() == primeiro_nome.lower() and contato2["sobrenome"].lower() == sobrenome.lower():
            contato_a_atualizar = contato2
        elif contato3 and contato3["nome"].lower() == primeiro_nome.lower() and contato3["sobrenome"].lower() == sobrenome.lower():
            contato_a_atualizar = contato3
        elif contato4 and contato4["nome"].lower() == primeiro_nome.lower() and contato4["sobrenome"].lower() == sobrenome.lower():
            contato_a_atualizar = contato4
        elif contato5 and contato5["nome"].lower() == primeiro_nome.lower() and contato5["sobrenome"].lower() == sobrenome.lower():
            contato_a_atualizar = contato5

        if not contato_a_atualizar:
            print("Contato não encontrado.")
            continue

        while True:
            print("\nO que você deseja atualizar?")
            print("Contato: " + contato_a_atualizar['nome'] + " " + contato_a_atualizar['sobrenome'])
            print("1 - Primeiro Nome")
            print("2 - Sobrenome")
            print("3 - Telefone")
            print("4 - Celular")
            print("5 - E-mail")
            print("6 - Aniversário")
            print("7 - Voltar ao menu principal")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                novo_nome = input("Digite o novo primeiro nome: ").strip()
                if novo_nome.isalpha() and len(novo_nome) <= 20:
                    contato_a_atualizar['nome'] = novo_nome
                    print("Nome atualizado!")
                else:
                    print("Nome inválido.")

            elif opcao == '2':
                novo_sobrenome = input("Digite o novo sobrenome: ").strip()
                if novo_sobrenome.isalpha() and len(novo_sobrenome) <= 20:
                    contato_a_atualizar['sobrenome'] = novo_sobrenome
                    print("Sobrenome atualizado!")
                else:
                    print("Sobrenome inválido.")

            elif opcao == '3':
                novo_telefone = input("Novo número de telefone: ").replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
                if not novo_telefone or (novo_telefone.isdigit() and len(novo_telefone) <= 15):
                    contato_a_atualizar['telefone'] = novo_telefone
                    print("Telefone atualizado!")
                else:
                    print("Telefone inválido.")

            elif opcao == '4':
                novo_celular = input("Novo número de celular: ").replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
                if novo_celular.isdigit() and len(novo_celular) <= 15:
                    contato_a_atualizar['celular'] = novo_celular
                    print("Celular atualizado!")
                else:
                    print("Celular inválido.")

            if opcao == '5':
                novo_email = input("Novo e-mail: ").strip().lower()
                while True:
                    permitido_local_chars = "abcdefghijklmnopqrstuvwxyz0123456789._+-"
                    permitido_domain_chars = "abcdefghijklmnopqrstuvwxyz0123456789.-"
                    partes = novo_email.split('@', 1)
                    if len(partes) == 2 and partes[0] and partes[1] and '.' in partes[1]:
                        local, dominio = partes
                        partes_dominio = dominio.rsplit('.', 1)
                        nome_dominio, tld = partes_dominio
                        if (
                            all(c in permitido_local_chars for c in local) and
                            local[0] not in '._+-' and local[-1] not in '._+-' and
                            '..' not in local and '__' not in local and '++' not in local and
                            all(c in permitido_domain_chars for c in dominio) and
                            dominio[0] != '-' and nome_dominio[-1] != '-' and
                            '--' not in dominio and
                            len(tld) >= 2 and tld.isalpha()
                        ):
                            contato_a_atualizar['email'] = novo_email
                            print("E-mail atualizado!")
                            break
                    print("E-mail inválido!")
                    novo_email = input("Novo e-mail: ").strip().lower()

            elif opcao == '6':
                novo_dia = input("Novo dia (DD): ").strip()
                novo_mes = input("Novo mês (MM): ").strip()
                novo_ano = input("Novo ano (AAAA): ").strip()
                if (novo_dia.isdigit() and len(novo_dia) == 2 and 1 <= int(novo_dia) <= 31 and
                    novo_mes.isdigit() and len(novo_mes) == 2 and 1 <= int(novo_mes) <= 12 and
                    novo_ano.isdigit() and len(novo_ano) == 4 and 1900 <= int(novo_ano) <= 2025):
                    contato_a_atualizar['aniversario'] = novo_dia + "/" + novo_mes + "/" + novo_ano
                    print("Aniversário atualizado!")
                else:
                    print("Data inválida.")

            elif opcao == '7':
                break
            else:
                print("Opção inválida.")

    elif comando == "5":
        primeiro_nome = input("Digite o primeiro nome do contato: ").strip()
        sobrenome = input("Digite o sobrenome: ").strip()

        removido = False
        if contato1 and contato1["nome"].lower() == primeiro_nome.lower() and contato1["sobrenome"].lower() == sobrenome.lower():
            contato1 = None
            removido = True
        elif contato2 and contato2["nome"].lower() == primeiro_nome.lower() and contato2["sobrenome"].lower() == sobrenome.lower():
            contato2 = None
            removido = True
        elif contato3 and contato3["nome"].lower() == primeiro_nome.lower() and contato3["sobrenome"].lower() == sobrenome.lower():
            contato3 = None
            removido = True
        elif contato4 and contato4["nome"].lower() == primeiro_nome.lower() and contato4["sobrenome"].lower() == sobrenome.lower():
            contato4 = None
            removido = True
        elif contato5 and contato5["nome"].lower() == primeiro_nome.lower() and contato5["sobrenome"].lower() == sobrenome.lower():
            contato5 = None
            removido = True

        if removido:
            print("Contato removido com sucesso.")
        else:
            print("Contato não encontrado.")

    elif comando == "6":
        print("Obrigado por usar a agenda.")
        break
    else:
        print("Opção inválida. Tente novamente.")
