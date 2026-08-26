# MOODSHOT v2.0

# variáveis

historico = []
personalizado = {}
filtro = "Nenhum"
foco = 10
tema = "Nenhum"
modo = "Escuro"



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
    print("Qual desses você deseja usar? (1 - Tema ||| 2 - Modo)")
    resposta = int(input("Digite: "))

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
        resp_tema = int(input("Digite qual você quer: "))

        temas_dici = {
            1: "Flores",
            2: "Céu",
            3: "Frutiger Aero",
            4: "Laranja",
            5: "Nenhum"
        }
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
            print("Resposta invalida! Retornando ao menu.")
            return tema_atual, modo_atual

    elif resposta == 2:
        print("Opção 2 - Modo")
        print("-------------------")
        print(f"Modo atual: {modo_atual}")
        print("-------------------")
        print("1 - Modo Escuro")
        print("2 - Modo Claro")
        print("-------------------")
        resp_modo = int(input("Digite qual você quer: "))

        modos_dici = {
            1: "Escuro",
            2: "Claro"
        }
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
            print("Resposta invalida! Retornando ao menu.")
            return tema_atual, modo_atual
    else:
        print("Resposta invalida! Retornando ao menu.")
        return tema_atual, modo_atual



# código

while True:
    print("-------------------")
    print("MOODSHOT")
    print("1 - Alterar Foco")
    print("2 - Filtros")
    print("3 - Predefinições")
    print("4 - Histórico de ações")
    print("5 - Sair")
    print("-------------------")

    opcao = int(input("Digite sua opção: "))

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
            f = float(input("Digite o novo foco: "))
            foco = foco_alt(f)
        elif resposta == "N":
            print("Operação cancelada.")
            print("Retornando ao menu...")
        else:
            print("Resposta invalida! Retornando ao menu.")

    elif opcao == 2:
        print("Opção 2 - Filtros")
        print("-------------------")
        print(f"Filtro atual: {filtro}")
        print("-------------------")
        print("1 - Filtros Default")
        print("2 - Filtros Predefinidos (novo)")
        print("3 - Retornar")
        print("-------------------")
        resposta = int(input("Digite sua opção: "))

        if resposta == 1:
            print("Filtros Default:")
            print("1 - Modo Viagem")
            print("2 - Modo Estudo")
            print("3 - Modo Encontro")
            print("4 - Modo PopArt")
            print("5 - Desativar Filtro")
            print("-------------------")
            resp_default = int(input("Digite sua opção: "))

            dicionario = {1: "Modo Viagem", 2: "Modo Estudo", 3: "Modo Encontro", 4: "Modo PopArt", 5: "Nenhum"}
            if resp_default in dicionario:
                filtro = dicionario[resp_default]
                print(f"Filtro modificado para: {filtro}")
                historico.append(f"Filtro modificado para: {filtro}")
                print("Retornando ao menu...")
            else:
                print("Resposta invalida! Retornando ao menu.")

        elif resposta == 2:
            print("Entrando na customização de filtros...")
            print(f"Seus filtros: {personalizado}")
            print("-------------------")
            print("1 - Criar nova predefinição")
            print("2 - Usar filtro já existente")
            print("3 - Retornar")
            print("-------------------")
            resp_predefn = int(input("Digite sua opção: "))

            if resp_predefn == 1:
                print("Opção 1 - Criar nova predefinição")
                print("-------------------")
                fc = float(input("Digite qual será o foco (num) do filtro: "))
                sat = float(input("Digite qual será a saturação do filtro: "))
                vin = float(input("Digite qual será o nível da vinheta do filtro: "))

                while True:
                    print("Você quer colocar uma cor matriz no filtro?")
                    resp_cor = input("Digite 'S' ou 'N': ").upper()
                    if resp_cor in ["S", "SIM"]:
                        cor = input("Digite a cor matriz do filtro: ")
                        break
                    elif resp_cor in ["N", "NAO", "NÃO"]:
                        cor = "Não tem cor Matriz."
                        break
                    else:
                        print("Resposta invalida! Digite novamente.")

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