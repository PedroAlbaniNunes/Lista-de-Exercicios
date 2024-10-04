import os
import random
# #Exercicio 1:
def f_limpaTela():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def f_genius():

    caminho = (r"C:\Users\ph\Desktop\ifes\programacao2-ifes\exercicio\sequencia.txt")
    f_limpaTela()
    i = 0
    n = random.randint(1,4)
    print(f'O número sorteado foi: {n}')
    x = input('Digite o número sorteado: ')
    y = str(n)
    if x == y:
        i += 1
    while x == y:
        n = random.randint(1,4)
        y = y + str(n)
        f_limpaTela()
        print(f'O número sorteado foi: {n}')
        x = input('Digite os números sorteados até o momento: ')
        i += 1

    f = open(caminho, "w")
    f.write("O maior pontuador fez ")
    f.write(str(i))
    f.write(" pontos")
    f.close()

    print('Você errou.')
    print(f'A sequencia correta é: {y}')



#Exercicio 2:
def f_menuAgenda():
    menu = '''
Menu Agendas:

1) Cadastrar telefone.
2) Visualizar agenda.
3) Sair.
'''

    x = input(menu)

    caminho = (r"C:\Users\ph\Desktop\ifes\programacao2-ifes\exercicio\listaTelefonica.txt")

    while x != '3':
        f_limpaTela()
        if x == '1':
            f_cadastrarTelefone(caminho)
        elif x == '2':
            f_visualizarAgenda(caminho)
        else:
            print('errou burrão')
        x = input(menu)
            

def f_cadastrarTelefone(caminho):
    f_limpaTela()
    nome = input('Digite o nome do contato: ')
    numero = input('Digite o número do contato: ')
    if len(caminho) == 1:
        f = open(caminho, "w")
        f.write(f'{nome}: {numero} \n')
        f.close()
    else:
        f = open(caminho, "a")
        f.write(f'{nome}: {numero} \n')
        f.close()

def f_visualizarAgenda(caminho):
    f_limpaTela()
    f = open(caminho, "r")
    lista = f.read()
    f.close()
    print(lista)


#Exercicio 3:
import pickle

#Cadastrar jogadores
def f_cadastrarJogador(listaJogadores):
    nome = input('Digite o nome do jogador a ser cadastrado: ')
    cpf = input('Digite o cpf do jogador; ')
    l = [nome, cpf]
    with open(listaJogadores, 'wb' ) as f:
        pickle.dump(l, f)

    return listaJogadores

#Nome jogadores
def f_nomeJogadores(listaJogadores, cpf):
    conteudo = listaJogadores.load()
    for (nome, cpfs) in conteudo.find(cpf):
        if cpfs == cpf:
            return nome
        
#listar jogadores
def f_listarJogadores(listaJogadores):
    if len(listaJogadores) > 0:
        print('Jogadores Cadastrados: ')
        with open(listaJogadores, 'rb') as f:
            l = pickle.load()
            for item in l:
                print(item)
    else:
        print('Nenhum jogador cadastrado. ')

#Cadastrar aposta
def f_cadastrarApostas(listaJogadores, listaApostas):
    numeros = input('Insira os números da aposta: ')
    with open(listaJogadores, 'rb') as f:
        l = pickle.load()
        for cpf in l:
            with open(listaApostas, 'wb') as g:
                pickle.dump(numeros, g)

#Listar apostas
def f_listarApostas(listaApostas):
    with open(listaApostas, 'rb') as f:
        l = pickle.load(f)
        for item in l:
            print(item)

#Exibir vencedores
def f_exibirVencedores(listaJogadores, listaApostas, premioPorBilhete):
    cpfs = {}
    with open(listaApostas, 'rb') as f:
        apostas = f
    cpfs = {'cpfs', f}
    p = premioPorBilhete / len(cpfs)
    for cpf in cpfs:
        print(f'{f_nomeJogadores(listaJogadores, cpf)} ({cpf}): R${p}')

#Sorteio
def f_vencedor(listaApostas, sorteados):
    apostados = {}
    with open(listaApostas, 'rb') as f:
        apostados = {f[0]}

    x = 0
    for n in apostados:
        if n in sorteados:
            x += 1
    
    return x == 6

def f_vencedoras(listaApostas, sorteados):
    l = {}
    i = 1
    with open(listaApostas, 'rb') as f:
        g = pickle.load(f)
    for aposta in g:
        if f_vencedor(listaApostas, sorteados):
            l[1] = aposta
            i += 1

def f_sorteio(listaApostas, listaJogadores):
    sorteados = {}
    sorteados = {'bilhete': {}}
    while sorteados['bilhete'] < 6:
        x = int(input('Digite um número entre 1 e 60 que ainda não foi digitado: '))

        if x >= 1 and x <= 60 not in sorteados['bilhete']:
            sorteados['bilhete'] += x
        else:
            print('Erro')
    
    premioTotal = int(input('Digite o valor do prêmio total: '))

    v = f_vencedoras(listaApostas, sorteados)
    
    f_limpaTela()

    if len(v) == 0:
        print('Ninguém venceu')
    else:
        print('Apostas vencedoras: ')
        premioPorBilhete = premioTotal / v
        i = 1
        with open(listaApostas, 'rb') as f:
            apostas = pickle.load(f)
        for apostas in v:
            print(f'Bilhete {i}')
            f_exibirVencedores(listaJogadores, listaApostas, premioPorBilhete)
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

    listaJogadores = (r'C:\Users\ph\Desktop\ifes\programacao2-ifes\exercicio\listaJogadores.bin')
    listaApostas = (r'C:\Users\ph\Desktop\ifes\programacao2-ifes\exercicio\listaApostas.bin')
    while x != '6':
        f_limpaTela()
        if x == '1':
            f_cadastrarJogador(listaJogadores)
        elif x == '2':
            f_listarJogadores(listaJogadores)
        elif x == '3':
            f_cadastrarApostas(listaJogadores,listaApostas)
        elif x == '4':
            f_listarApostas(listaApostas)
        elif x == '5':
            f_sorteio(listaJogadores)
        else:
            print('Opção inválida. Burro.')

        x = input(menu)
def main():

    f_menuBolao()

if __name__ == '__main__':
    main()