# MOODSHOT v2.0

# variáveis

historico = []
personalizado = {}
filtro = "Nenhum"
foco = 10
tema = "Nenhum"
modo = "Escuro"
opcao = "oi"


# funções


def foco_alt(f):
    foco_val = f
    print(f"Novo foco: {foco_val}")
    print("Retornando ao menu...")
    historico.append(f"O foco foi modificado. ({foco_val})")
    return foco_val


def filtro_person():
    while True:
        resposta = input("Digite o nome (ou retornar): ")
        if resposta.lower() in ["retornar", "return"]:
            print("OK! Retornando ao menu...")
            break
        elif resposta in personalizado:
            filtro_selecionado = personalizado[resposta]
            print(f"Filtro modificado para: {filtro_selecionado}")
            historico.append(f"Filtro modificado para: {resposta}")
            return resposta


def predefinicoes(tema_atual, modo_atual):
    while True:
        print("Qual desses você deseja usar? (1 - Tema ||| 2 - Modo ||| 3 - Retornar)")
        resposta = input("Digite: ")
        if resposta.isdigit():
            resposta = int(resposta)
            break
        else:
            print('Resposta Inválida! Tente novamente.')

    if resposta == 1:
        print("Opção 1 - Tema")
        print("-------------------")
        print(f"Tema atual: {tema_atual}")
        print("-------------------")
        print("1 - Tema Flores")
        print("2 - Tema Céu")
        print("3 - Tema Frutiger Aero")
        print("4 - Tema Laranja")
        print("5 - Desativar Tema")
        print("-------------------")
        while True:
            resp_tema = input("Digite qual você quer: ")
            temas_dici = {
            1: "Flores",
            2: "Céu",
            3: "Frutiger Aero",
            4: "Laranja",
            5: "Nenhum"
            }
            if resp_tema not in ["1", "2", "3", "4", "5"]:
                print("Resposta Inválida! tente novamente")
            else:
                resp_tema = int(resp_tema)
                break
        if resp_tema in temas_dici:
            novo_tema = temas_dici[resp_tema]
            print("-------------------")
            print(f"Tema atual: {novo_tema}")
            print("-------------------")
            print(f"Tema modificado para: {novo_tema}")
            historico.append(f"Tema modificado para: {novo_tema}")
            print("Retornando ao menu...")
            return novo_tema, modo_atual
        else:
            print("Resposta Inválida! Retornando ao menu.")
            return tema_atual, modo_atual

    elif resposta == 2:
        print("Opção 2 - Modo")
        print("-------------------")
        print(f"Modo atual: {modo_atual}")
        print("-------------------")
        print("1 - Modo Escuro")
        print("2 - Modo Claro")
        print("-------------------")
        while True:
            resp_modo = input("Digite qual você quer: ")

            modos_dici = {
            1: "Escuro",
            2: "Claro"
            }

            if resp_modo not in ["1", "2"]:
                print("Resposta Inválida! tente novamente")
            else:
                resp_modo = int(resp_modo)
                break
        if resp_modo in modos_dici:
            novo_modo = modos_dici[resp_modo]
            print("-------------------")
            print(f"Modo atual: {novo_modo}")
            print("-------------------")
            print(f"Modo modificado para: {novo_modo}")
            historico.append(f"Modo modificado para: {novo_modo}")
            print("Retornando ao menu...")
            return tema_atual, novo_modo
        else:
            print("Resposta Inválida! Retornando ao menu...")
            return tema_atual, modo_atual
    elif resposta == 3:
        print('Retornando ao menu...')
        return tema_atual, modo_atual
    else:
        print("Resposta Inválida! Retornando ao menu.")
        return tema_atual, modo_atual



# código

while True:
    while opcao != int:
        print("-------------------")
        print("MOODSHOT")
        print("1 - Alterar Foco")
        print("2 - Filtros")
        print("3 - Predefinições")
        print("4 - Histórico de ações")
        print("5 - Sair")
        print("-------------------")

        opcao = input("Digite sua opção: ")
        if opcao in ["1","2","3","4","5"]:
            opcao = int(opcao)
            break

        else:
            print('Opção inválida! Tente novamente.')

    if opcao < 1 or opcao > 5:
        print("Opção invalida!")

    elif opcao == 1:
        print("Opção 1 - Alterar Foco")
        print(f"Foco atual: {foco}")
        print("-------------------")
        print("Você deseja alterar o foco?")
        print("S - N")
        resposta = input("Digite: ").upper()
        if resposta == "S":
            while True:
                    f = input("Digite o novo foco: ")
                    if f.isdigit(): # <--- não lembro se vimos "isdigit()" ou não, mas optei por usar por facilitar bastante
                        f = float(f)
                        if f < 0:
                            print("Valor invalido! Tente novamente.")
                        else:
                            foco = foco_alt(f)
                            break
                    else:
                        print('Valor invalido! Tente novamente.')
        elif resposta == "N":
            print("Operação cancelada.")
            print("Retornando ao menu...")
        else:
            print("Resposta Inválida! Retornando ao menu.")

    elif opcao == 2:
        print("Opção 2 - Filtros")
        print("-------------------")
        print(f"Filtro atual: {filtro}")
        print("-------------------")
        print("1 - Filtros Default")
        print("2 - Filtros Predefinidos (novo)")
        print("3 - Retornar")
        print("-------------------")

        while True:
            resposta = input("Digite sua opção: ")
            if resposta in ["1", "2", "3"]:
                resposta = int(resposta)
                break
            else:
                print("Resposta Inválida! Tente novamente.")

        if resposta == 1:
            print("Filtros Default:")
            print("1 - Modo Viagem")
            print("2 - Modo Estudo")
            print("3 - Modo Encontro")
            print("4 - Modo PopArt")
            print("5 - Desativar Filtro")
            print("-------------------")
            while True:
                resp_default = input("Digite sua opção: ")
                if resp_default in ["1", "2", "3", "4", "5"]:
                    resp_default = int(resp_default)
                    break
                else:
                    print("Resposta Inválida! Tente novamente.")

            dicionario = {1: "Modo Viagem", 2: "Modo Estudo", 3: "Modo Encontro", 4: "Modo PopArt", 5: "Nenhum"}

            if resp_default in dicionario:
                filtro = dicionario[resp_default]
                print(f"Filtro modificado para: {filtro}")
                historico.append(f"Filtro modificado para: {filtro}")
                print("Retornando ao menu...")

            else:
                print("Resposta Inválida! Retornando ao menu.")


        elif resposta == 2:
            print("Entrando na customização de filtros...")
            print(f"Seus filtros: {personalizado}")
            print("-------------------")
            print("1 - Criar nova predefinição")
            print("2 - Usar filtro já existente")
            print("3 - Retornar")
            print("-------------------")

            while True:

                resp_predefn = input("Digite sua opção: ")

                if resp_predefn in ["1", "2", "3"]:
                    resp_predefn = int(resp_predefn)
                    break

                else:
                    print("Resposta Inválida! Tente novamente.")

            if resp_predefn == 1:

                print("Opção 1 - Criar nova predefinição")
                print("-------------------")

                while True:

                    fc = input("Digite qual será o foco (num) do filtro: ")

                    if fc.isdigit():
                        fc = float(fc)
                        break

                    else:
                        print("Resposta Inválida! Tente novamente.")

                while True:

                    sat = input("Digite qual será a saturação do filtro: ")

                    if sat.isdigit():
                        sat = float(sat)
                        break

                    else:
                        print("Resposta Inválida! Tente novamente.")

                while True:

                    vin = input("Digite qual será o nível da vinheta do filtro: ")

                    if vin.isdigit():
                        vin = float(vin)
                        break

                    else:
                        print("Resposta Inválida! Tente novamente.")

                while True:

                    print("Você quer colocar uma cor matiz no filtro?")

                    resp_cor = input("Digite 'S' ou 'N': ").upper()

                    if resp_cor in ["S", "SIM"]:
                        cor = input("Digite a cor matiz do filtro: ")
                        break

                    elif resp_cor in ["N", "NAO", "NÃO"]:
                        cor = "Não tem cor Matiz."
                        break

                    else:
                        print("Resposta Inválida! Digite novamente.")

                nome = input("Digite o nome do filtro: ")

                personalizado[nome] = (fc, sat, vin, cor)
                historico.append(f"O Usuário criou um novo filtro: {nome}")

                print(f"Filtro {nome} criado com sucesso.")

                print("Deseja ativá-lo agora?")

                resp_ativar = input("Digite 'S' ou 'N': ").upper()

                if resp_ativar in ["S", "SIM"]:
                    filtro = nome
                    foco = fc
                    print(f"Filtro ativado")
                    historico.append(f"Filtro modificado para: {filtro}")

                elif resp_ativar in ["N", "NÃO", "NAO"]:
                    print("Ok! Retornando ao menu...")

                else:
                    print("Resposta inválida. Você pode ativá-lo mais tarde. Retornando ao menu...")

            elif resp_predefn == 2:

                if not personalizado:
                    print("-------------------")
                    print("Aviso: Nenhum filtro personalizado cadastrado!")
                    print("Crie um filtro primeiro.")
                    print("Retornando ao menu...")

                else:
                    print(personalizado)
                    print("Você deseja usar um desses filtros?")
                    resp_usar = input("Digite 'S' ou 'N': ").upper()

                    if resp_usar in ["S", "SIM"]:
                        print('Digite o nome do filtro desejado (ou digite "retornar" para sair):')
                        res_filtro = filtro_person()

                        if res_filtro:
                            filtro = res_filtro

                            if res_filtro in personalizado:
                                foco = personalizado[res_filtro][0]

                    elif resp_usar in ["N", "NAO", "NÃO"]:
                        print("Ok! Retornando ao menu...")

                    else:
                        print("Resposta inválida! Retornando ao menu...")

            elif resp_predefn == 3:
                print("Retornando ao Menu...")

        elif resposta == 3:
            print("Retornando ao Menu...")

    elif opcao == 3:
        print("Abrindo menu de predefinições...")
        print("-------------------")
        print("1 - Tema")
        print("2 - Modo")
        print('3 - Retornar')
        print("-------------------")
        tema, modo = predefinicoes(tema, modo)

    elif opcao == 4:
        print("Opção 4 - Histórico de ações")
        print("-------------------")
        print("Aqui está seu histórico de ações:")
        if not historico:
            print("Você não fez nenhuma ação recentemente.")
        else:
            print(historico)
        print("Retornando ao menu...")

    elif opcao == 5:
        print("Obrigado por usar o MoodShot!")
        break
