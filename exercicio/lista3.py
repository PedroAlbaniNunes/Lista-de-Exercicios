import os
#Exercicio 1:
def f_adulto(l):
    nome = []
    for n in l:
        nome.append(n)

    for t in nome:
        if l[t][0] < 18:
            del l[t]

    print(l)

#Exercicio 2:
#Cadastrar telefones
def f_cadastrarTelefone(agenda):
    nome = str(input('Escreva o nome que deseja que o contato seja salvo: '))
    tel = str(input('Digite o número de telefone desse contato: '))

    agenda[nome] = tel

    print('Contato adcionado com sucesso')

#Visualizar agenda
def f_visualizarAgenda(agenda):
    f_limpaTela()
    if len(agenda) > 0:
        print('Contatos salvos:')
        for nome in agenda:
            print(nome+':', agenda[nome])
        
    else:
        print('Sem contatos salvos :D')

#Principal
def f_menuAgenda():
    menu = '''
Menu para cadastro telefônico:

1) Cadastrar telefone
2) Visualizar agenda
    
Selecione uma das opções: 
'''
    
    agenda = {}
    
    selecao = input(menu)
    while (selecao == '1') or (selecao == '2'):
        f_limpaTela()
        if selecao == '1':
            f_cadastrarTelefone(agenda)
        elif selecao == '2':
            f_visualizarAgenda(agenda)

        selecao = input(menu)
    
    print('Tchauzin')



#Exercicio 3:
#Limpar tela
def f_limpaTela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#Cadastrar jogadores
def f_cadastrarJogador(jogadores):
    nome = input('Digite o nome: ')
    cpf = input('Digite o cpf: ')

    jogadores[cpf] = nome

    return jogadores

#Nome dos jogadores
def f_nomeJogadores(jogadores,cpf):
    for (nome, cpfs) in jogadores[cpf]:
        if cpfs == cpf:
            return nome

#Listar jogadores
def f_listarJogadores(jogadores):
    if len(jogadores) > 0:
        print('Jogadores cadastrados: ')
        for nome in jogadores:
            print(nome, '-', jogadores[nome])
    else:
        print('Nenhum jogaor cadastrado.')

#Cadastrar apostar
def f_cadastrarApostas(jogadores,apostas):
    numeros = input('Insira os numeros da aposta: ')

    for cpf in jogadores:
        apostas[numeros] = cpf

#Listar apostas
def f_listarApostas(apostas):
    for i in len(apostas):
        print(apostas)

def f_exibirVencedores(jogadores, apostas, premioPorBilhete):
    cpfs = {}
    cpfs = {'cpfs': apostas}
    p = premioPorBilhete / len(cpfs)
    for cpf in cpfs:
        print(f'{f_nomeJogadores(jogadores,cpf)} ({cpf}): R${p}')

#Sorteio
def f_vencedor(apostas, sorteados):
    apostados = {}
    apostados = apostas[0]

    x = 0
    for n in apostados:
        if n in sorteados:
            x += 1

    return x == 6

def f_vencedoras(apostas,sorteados):
    l = {}
    i = 1
    for aposta in apostas:
        if f_vencedor(aposta,sorteados):
            l[i] = apostas
            i += 1


def f_sorteio(apostas, jogadores):
    sorteados = {}
    sorteados = {'bilhete': {}}
    while sorteados['bilhete'] < 6:
        x = int(input('Digite um número entre 1 e 60 que ainda não foi digitado: '))

        if x >= 1 and x <= 60 not in sorteados['bilhete']:
            sorteados['bilhete'] += x
        else:
            print('erro')

    premioTotal = int(input('Digite o valor do premio: '))

    v = f_vencedoras(apostas, sorteados)

    f_limpaTela()

    if len(v) == 0:
        print('Ngm venceu')
    else:
        print('Apostas vencedoras: ')
        premioPorBilhete = premioTotal / v
        i = 1
        for apostas in v:
            print(f'Bilhete {i}')
            f_exibirVencedores(jogadores,apostas,premioPorBilhete)
            print()
            i += 1

#Menu bolão 
def f_menuBolao():
    menu = '''
Escolha uma opção:

1) Cadastrar jogador
2) Visualizar jogadores cadastrados
3) Cadastrar bilhete
4) Visualizar bilhetes cadastrados
5) Sorteio
6) Sair
'''
    x = input(menu)

    jogadores = {}
    apostas = {}

    while x != '6':
        f_limpaTela()
        if x == '1':
            f_cadastrarJogador(jogadores)
        elif x == '2':
            f_listarJogadores(jogadores)
        elif x == '3':
            f_cadastrarApostas(jogadores,apostas)
        elif x == '4':
            f_listarApostas(apostas)
        elif x == '5':
            f_sorteio(jogadores)
        else:
            print('Opção inválida. Burro.')

        x = input(menu)
            


#Exercicio 4:
def f_maisVelho(data1, data2):
    d1,m1,a1 = data1
    d2,m2,a2 = data2
    if (a1 > a2):
        return False
    if (a1 < a2):
        return True
    if (m1 > m2):
        return False
    if (m2 > m1):
        return True
    return d1 < d2

def f_primeiraEtapa(candidatos, areas):
    passou = {}
    for cod in areas:
        for insc in candidatos:
            if insc in areas[cod]:
                if candidatos[insc][2] > 60:
                    passou[cod] = (candidatos)

def f_segundaEtapa(candidatos, areas, passou):
    n = 0
    for cod in passou:
        if len(passou[cod]) == 1:
            print(f'O candidato {candidatos[cod]} passou')
        elif len(passou[cod]) < 1:
            print('Ninguém passou')
        else:
            for insc in candidatos:
                data = candidatos[insc][1]
                f_maisVelho(data,)
            

#Exercicio 5:
def f_filtro(infratores, data_hoje,anterior):
    filtrado = []
    data_corte = (data_hoje[0],data_hoje[1],data_hoje[2]-1)
    for infracao in infratores:
        data = infracao[1]
        if anterior(data_corte, data):
            filtrado.append(infracao)
    return filtrado

def f_pontos(naturezas, infratores, veiculos, cnh):
    pontos = 0
    for (cod, data, placa, natureza) in infratores:
        proprietario = veiculos[placa][0]
        if proprietario == cnh:
            pontos += naturezas[natureza]
    return pontos

def f_apreensao(motoristas, veiculos, infratores, naturezas, data, placa,cnh):
    if f_maisVelho(motoristas[cnh][1], data) == True:
        print('Apreende')
    if f_pontos(naturezas, infratores, veiculos, cnh) > 20:
        print('Apreende')
    if placa not in veiculos:
        print('Golpe')

#Exercicio 6:
def f_treino(exercicios, alunos, treinos,aluno, grupo):
    saida = ()
    for login in alunos:
        if aluno == login:  
            for (___, series, rep, tipo) in treinos[login]:
                if grupo == tipo:
                    for nome in exercicios[tipo]:
                        saida.append(f'\n+ {nome} - {series} de {rep}')

    return  print(f'Aluno: {aluno} +\n+ Grupo: {grupo} {saida}') 

def f_naoFaz(exercicio, alunos, treinos):
    aluno = input('Fala o nome do caba ai: ')
    if aluno == alunos[aluno][0]:
        if alunos == treinos:
            for (cod, __, __, __) in treinos:
                if exercicio not in treinos[aluno]:
                    print(exercicio[cod])

def f_veriricar(alunos, exercicios, treinos, aluno):
    login = input('Insira o login: ')
    senha = input('Insira a senha: ')
    if login in alunos:
        senha1 = alunos[login][1]
        if senha == senha1:
            grupo = input('Insira o grupo: ')
            if grupo in treinos[aluno]:
                f_treino(exercicios, alunos, treinos, aluno, grupo)
            else:
                print('Tem não')
        else:
            print('Senha incorreta')
            senha = input('Insira a senha:')
    else:
        print('Login inválido.')
        login = input('Insira o login: ')

#Exercicio 7:
def f_quantidadeSuficiente(clientes, produtos, pedidos, cod):
    quantidade_necessaria = 0
    quantidade_estocada = 0
    for chave in pedidos:
        if cod in pedidos[chave]:
            quantidade_necessaria += pedidos[chave][3]
        quantidade_estocada = produtos[cod][2]
        if quantidade_estocada < quantidade_necessaria:
            return (f'Quantidade insuficiente')
        else:
            return (f'Quantidade suficiente')

def f_impressao(clientes, produtos, pedidos, cod):
    for chave in pedidos:
        if cod == pedidos:
            quantidade = pedidos[cod][3]
            valor_unitario = produtos[pedidos[cod][2]][0]
            nome_produto = produtos[pedidos[cod][2]][1]
            valor_total = valor_unitario * quantidade
            return (f'Pedido #{cod}: +\n+ {nome_produto} +\n+ Qtd: {quantidade} +\n+ Valor unitário: R${valor_unitario} +\n+ Valor total: R${valor_total}')

def f_custoTotal(clientes, produtos, pedidos, cod):
    cpf, estado, l = pedidos[cod]
    preco_total = 0
    for (prod, qnt) in l:
        preco, nome, estoque = produtos[prod]
        preco_total += (preco * qnt)

    return preco_total

def f_cadaCliente(clientes, produtos, pedidos):
    for cpf in clientes:
        nome, email = clientes[cpf]
        for cod in pedidos:
            if cpf in pedidos[cod]:
                valor_gasto = f_custoTotal(clientes, produtos, pedidos, cod)
        print(f'O cliente {nome} já gastou um valor total de: R$ {valor_gasto}')


#Exercicio 8:



#Exercicio 9:


#Exercicio 10:
def f_correcao(historico, contas):
    corretos = {}
    for n in contas:
        corretos[n] = 0
    
    for t in historico:
        valor,numero,operacao = historico[t]
        if operacao	== '1':
            corretos[n] += valor
        else:
            corretos[n] -= valor

    return corretos

def f_invalidas(corretos, contas):
    invadidas = {}
    for n in contas:
        if corretos[n] != contas[n][0]:
            invadidas[n] = (corretos[n], contas[n][0])
    return invadidas

def f_prejuizo(invadidas):
    prejuizo = 0

    for n in invadidas:
        if invadidas[n][1] < 0:
            prejuizo += abs(invadidas[n][1] + invadidas[n][0])
        else:
            prejuizo += abs(invadidas[n][1] - invadidas[n][0])

    return prejuizo
def main():


    candidatos = {}
    areas = {}

    candidatos = {'123': ('Pedro', (20, 6, 2004), 10, 5),
                  '234': ('Cleiton', (12, 9, 1983), 7, 7),
                  '345': ('Maria', (1, 12, 2005), 8, 10)}
    
    areas = {'789': ('Enfermagem', ['123', '345']),
             '891': ('Computaria', ['123', '234']),
             '546': ('Direito', ['234', '345'])}
 

if __name__ == '__main__':
    main()