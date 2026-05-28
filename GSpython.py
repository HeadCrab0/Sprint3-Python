# Variaveis e Listas
nomes = []
plantacoes = []
temperaturas = []
umidades = []

def cadastrar_plantacao():  # Cadastro de Plantações + Fazendas
    nome = input('Digite o nome da fazenda: ').lower()
    tipo = input('Digite o tipo de plantação: ')
    temp = float(input('Digite a temperatura: '))
    umidade = float(input('Digite a umidade: '))

    umidades.append(umidade)
    temperaturas.append(temp)

    nova_planta = [tipo, temp, umidade]

    if nome in nomes:
        x = nomes.index(nome)
        plantacoes[x].append(nova_planta)
        print("Nova plantação adicionada à fazenda existente.")
    else:
        nomes.append(nome)
        plantacoes.append([nova_planta])
        print("Nova fazenda e plantação criadas.")

def relatorio():
    for i in range(len(nomes)):
        print(f"\nFazenda: {nomes[i]}")
        for plantacao in plantacoes[i]:
            print(f" - Tipo: {plantacao[0]}, Temp: {plantacao[1]}C, Umidade: {plantacao[2]}%")

while True:
    # Menu
    print('-----------------------')
    print('1 - Cadastrar Plantação')
    print('2 - Monitorar Umidade')
    print('3 - Checar Temperatura')
    print('4 - Emitir Alerta Agrícola')
    print('5 - Relatório da Fazenda')
    print('6 - Sobre o projeto')
    print('7 - Sair')

    opcao = int(input('Digite sua opcao: '))

    if opcao == 1: #Cadastrar Plantação
        cadastrar_plantacao()


    elif opcao == 2:
        print('')
    elif opcao == 3:
        print('')
    elif opcao == 4:
        print('')
    elif opcao == 5:
        relatorio()
    elif opcao == 6:
        print('')
    elif opcao == 7:
        break
    else:
        print('Opção invalida! Tente novamente.')