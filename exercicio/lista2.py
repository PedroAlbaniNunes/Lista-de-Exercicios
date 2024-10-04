import random
import os
#Exercicio 1:
def f_bonus(l):
    maior_tempo = 0
    for (_,tempo,_) in l:
        if (tempo > maior_tempo):
            maior_tempo = tempo
    for (nome,tempo,salario) in l:
        if (tempo == maior_tempo):
            print('%s vai receber %.2f' %(nome,salario*1.1))


#Exercicio 2:
def f_lucro(l):
    menos_20 = int()
    maior_25 = float()

    menos_20 = 0
    maior_25 = 0
    for (custo, venda) in l:
        if (custo * 1.2 > venda):
            menos_20 += 1
        if (custo * 1.25 < venda):
            maior_25 += 1

    porc = (maior_25/len(l)) * 100

    print(f'Tem {menos_20} produtos que dão menos que 20% de lucro')
    print(f'{porc}% dos produtos dão lucro a mais que 25% de lucro')


#Exercicio 3:
import lista
def f_planoCartesiano(t1,t2,t3):

    x1,y1 = t1
    x2,y2 = t2
    x3,y3 = t3

    l = [(x1,y1,1),(x2,y2,1),(x3,y3,1)]

    return lista.f_determinanteMatriz(l) == 0


#Exercicio 4:
def f_partidaAdestinoFinalB(voos,a,b):
    
    for(numero,companhia,voo) in voos:
        if voo[0] == a and voo[-1] == b:
            print(f'O número da companhia é {numero} e o seu nome é {companhia}.')


def f_partidaAEscalaB(voos,a,b):
    i = 0
    for (numero,companhia,voo) in voos:
        for i in range(len(voo)):
            if (voo[0] == a) and (voo[i] == b):
                print(f'O número da companhia é {numero} e o seu nome é {companhia}')


def f_vooDireto(voos,a,b):
    for (numero,companhia,voo) in voos:
        i = 0
        while i < len(voo):
            if (voo[i] == a) and (voo[i+1] == b):
                print(f'O número da companhia é {numero} e o seu nome é {companhia}')
            i += 1


#Exercicio 5:
def f_empatesCopa(qnt_jogos, classificacao):
    soma = 0
    for (_,pontos) in classificacao:
        soma += pontos
    
    empates = 3*qnt_jogos - soma

    return empates


#Exercicio do Bolão:

def f_limpaTela():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
		

def f_listarJogadores(l):
	if len(l) > 0:
		print("Jogadores cadastrados:")
		
		for (nome, cpf) in l:
			print(nome, "-", cpf)
	
	else:
		print("Nenhum jogador cadastrado até agora.")
	
def f_nomeJog(jogs, cpf):
	for (n, c) in jogs:
		if c == cpf:
			return n
	
def f_existeCPF(c, l):
	for (nome, cpf) in l:
		if cpf == c:
			return True
	
	return False
	
def f_cadastrarJogador(l):
	f_listarJogadores(l)
	
	nome = input("Digite o nome do jogador: ")
	cpf = input("Digite o cpf do jogador: ")
	
	while f_existeCPF(cpf, l):
		print("Erro: CPF já existente.")
		cpf = input("Digite o cpf do jogador: ")
	
	l.append( (nome, cpf) )
	print("Jogador inserido com sucesso.")


def f_inserirNumerosApostados():
	l = []
	
	x = int(input("Quantos números neste bilhete? "))
	
	while x < 6 or x > 15:
		x = int(input("Ooops... digite um número entre 6 e 15: "))
	
	while len(l) < x:

		
		n = int(input("Digite um número: "))
		if n < 1 or n > 60 or n in l:
			print("Número inválido.")
		else:
			l.append(n)

	return l
	
def f_inserirCPFs(jogs):
	l = []
	f_listarJogadores(jogs)
	
	n = int(input("Quantos jogadores neste bilhete? "))
	
	for i in range(n):
		cpf = input("Digite o CPF do jogador: ")
		
		while not f_existeCPF(cpf, jogs):
			cpf = input("CPF inválido. Tente outro: ")
			
		l.append(cpf)
		
	return l
			
	
def f_cadastrarApostas(jogs, apostas):
	numeros = f_inserirNumerosApostados()
	cpfs = f_inserirCPFs(jogs)
	
	apostas.append( (numeros, cpfs) )
	print("Aposta cadastrada com sucesso.")


def f_listarApostas(jogs, apostas):
	
	for i in range(len(apostas)):
		numeros, cpfs = apostas[i]
		
		print(f'Bilhete {i+1}:')
		
		print('Números: ', end='')
		
		for n in numeros: print(n, end=' ')
		print()
		
		print('Jogadores:')
		for cpf in cpfs:
			print(f_nomeJog(jogs, cpf), '-', cpf)
			
		print()
			
def f_vencedora(aposta, sorteados):
	apostados = aposta[0]
	
	x = 0
	for n in apostados:
		if n in sorteados: x += 1
		
	return x == 6
	
def f_vencedoras(apostas, sorteados):
	l = []
	
	for aposta in apostas:
		if f_vencedora(aposta, sorteados):
			l.append(aposta)
		
	return l
	
	
def f_exibirVencedores(jogs, aposta, premioPorBilhete):
	cpfs = aposta[1]
	p = premioPorBilhete / len(cpfs)
	
	for cpf in cpfs:
		print(f'{f_nomeJog(jogs, cpf)} ({cpf}): R${p}')
	
	
def f_sorteio(jogs, apostas):
	sorteados = []
	
	while len(sorteados) < 6:
		x = int(input("Digite um número entre 1 e 60 que vc ainda não digitou: "))
		
		if x >=1 and x <= 60 and x not in sorteados:
			sorteados.append(x)
		else:
			print("Burrão")
	
	premioTotal = int(input("Digite o prêmio total: R$"))
	
	v = f_vencedoras(apostas, sorteados)
	
	f_limpaTela()
	
	if len(v) == 0:
		print("Não houve vencedores.")
	else:
		print("Apostas Vencedoras:")
		premioPorBilhete = premioTotal / len(v)
		
		i = 1
		for aposta in v:
			print(f'Bilhete {i}:')
			f_exibirVencedores(jogs, aposta, premioPorBilhete)
			print()
			i += 1



def f_mainBolão():
	print("Seja bem vindo ao Bolão")
	
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
	
	jogs = []
	apostas = []
	
	while x != "6":
		f_limpaTela()
		if x == "1":
			f_cadastrarJogador(jogs)
		elif x == "2":
			f_listarJogadores(jogs)
		elif x == "3":
			f_cadastrarApostas(jogs, apostas)
		elif x == "4":
			f_listarApostas(jogs, apostas)
		elif x == "5":
			f_sorteio(jogs, apostas)
		else:
			print("Opção inválida. Tente novamente")
		
			
		x = input(menu)
	
	print("Tchau")




def f_genius():

	f_limpaTela()
	n = random.randint(1,4)
	print(f'O número sorteado foi {n}')
	x = str(input('Digite a sequência. '))
	y = str(n)
	while x == y:
		n = random.randint(1,4)
		y = y + str(n)
		f_limpaTela()
		print(f'O número sorteado foi {n}')
		x = str(input('Digite a sequência. '))
		
	print('Você errou D;')
	print(f'A sequência correta era {y}')

