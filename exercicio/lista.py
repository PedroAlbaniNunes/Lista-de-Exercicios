#Exercicio 1
def f_paresRegre():
    l = list()
    n = int()

    n = 1
    while n <= 100:
        if (n % 2 == 0):
            l.append(n)
        n += 1

    l.sort()
    l.reverse()
    return l


#Exercicio 2


def f_metadePrint():
    l = list()
    i = int()
    n = int()

    i = 1
    while i <= 10:
        n = int(input())
        n = n/2
        l.append(n)
        i+=1

    print(l)

#Exercicio 3


def f_leit(n):
    l = list()
    k = int()
    i = int()

    i = 1

    while i <= n:
        k = int(input())
        l.append(k)
        i+=1

    return l


#Exercicio 4

def f_ocorre(l:list,j:int)->int:
    i = int()
    n = int()

    i = 0
    n = 0

    while i < len(l):
        if j == l[i]:
            n += 1
        i += 1

    return n


#Exercicio 5

def f_maxList(l):
    maior = l[0]

    for x in l:
        if (x > maior):
            maior = x

    return maior


#Exercicio 6

def f_maxPos(l):
    maior = int()
    i = int()
    i = 0
    maior_pos = f_maxList(l)

    while i < len(l):
        if maior_pos == l[i]:
            maior = i
        i += 1

    return maior
    

#Exercicio 7

def f_troca(l, i, j):
    aux = l[i]
    l[i] = l[j]
    l[j] = aux 

def f_reverse(l):
    i = int()
    j = int()
    aux = int()
    
    i = 0
    j = len(l) - 1
    

    while (i < j):  
        f_troca(l, i, j)
        i += 1
        j -= 1
        

#Exercicio 8
        
def f_fibonacci(n):
    l = list()

    if n == 1:
        l = [1]
    elif n == 2:
        l = [1,1]
    else:
        l = [1,1]

    for i in range(n-2):
        l.append(l[-1]+l[-2])

    return l


#Exercicio 9

def f_ParouImpar(a,b):
    abscissas = int()
    ordenadas = int()
    resultado = int()

    for j in a:
        if j % 2 == 0:
            abscissas += 1

    for i in b:
        if i % 2 != 0:
            ordenadas += 1


    if ordenadas <= abscissas:
        resultado = 0
        for abscissas in a:
            resultado += abscissas
            print(resultado)
    else:
        resultado = 1
        for ordenadas in b:
            resultado *= ordenadas
            print(resultado)


#Exercicio 10
            
def f_multiplos(k,n):
    i = int()
    l = list()
    i = 1

    while i <= k:
        l.append(i * n)
        i += 1

    return l


#Exercicio 11

def f_mediaAlunos(n,l):
    media_turma = float()
    nota_total = float()
    n_alunos = int()

    n_alunos = 0
    nota_total = 0
    if (n >= 0) and (n <= 100):
        for notas in range(n):
            nota_total = nota_total + l[notas]
        
        media_turma = nota_total / n

        for i in range(n):
            if l[i] > 60:
                n_alunos += 1
        print(media_turma)
        print(n_alunos)


#Exercicio 12
    
def f_mediaTemperatura(n,l):
    media_termperatura = float()
    temperatura_total = float()
    n_temperatura = int()

    n_temperatura = 0
    temperatura_total = 0

    for temp in range(n):
        temperatura_total = temperatura_total + l[temp]
    
    media_termperatura = temperatura_total / n

    for i in range(n):
        if l[i] < media_termperatura:
            n_temperatura += 1

    print(n_temperatura)


#Exercicio 13

def f_iguais(l1,l2):
    j = int()
    n = int()

    j = len(l1)
    n = 0
    for i in range(j):
        if l1[i] == l2[i]:
            n += 1
        
    print(n)


#Exercicio 14
def f_salarios(n,nome,salario):
    media_salario = float()
    total_salario = float()
    nome_lista = list()

    total_salario = 0
    for sal in range(n):
        total_salario += salario[sal]

    media_salario = total_salario / n

    for nomes in range(n):
        if salario[nomes] > media_salario:
            nome_lista.append(nome[nomes])
    
    print(media_salario)
    print(nome_lista)



#Exercicio 15
    
def f_sublista(l,x,y):
    l2 = list()
    
    for i in range(len(l)):
        if (l[i] < x) and (l[i] > y):
            l2.append(l[i])

    return l2


#Exercicio 16:

def f_semRepet(l):
    l2 = list()
       
    l2 = [l[0]]

    for i in l:
        if(i != l2[-1]):
            l2.append(i)
    return l2

def f_trocaCartas(l1,l2):
    n1 = int()
    n2 = int()

    l1 = f_semRepet(l1)
    l2 = f_semRepet(l2)

    n1 = 0
    for i in l1:
        if (i not in l2):
            n1 += 1

    n2 = 0
    for i in l2:
        if (i not in l1):
            n2 += 1


    return min(n1,n2)


#Exercicio 17:

def f_criaMatriz(m,n):
    M = []

    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(0)
        M.append(linha)
    
    return M


#Exercicio 18:

def f_formataMatriz(M):
    
    for linha in M:
        for elemento in linha:
            print(elemento, end="\t")
        print()


#Exercicio 19:

def f_somaMatriz(m1:list,m2:list):
    m3 = list()
    
    m3 = []
    for linha in range(len(m1)):
        soma = []
        for coluna in range(len(m1[0])):
            soma.append(m1[linha][coluna]+m2[linha][coluna])
        m3.append(soma)

    return m3


#Exercicio 20:
def f_valorNotas(m,n):
    tab = list()
    notas = list()

    tab = []

    for i in range(m):
        notas = []
        for j in range(n):
            notas.append(input())
        tab.append(notas)


#Exercicio 21

def f_matrizIdentidade(matriz):
    linhas = len(matriz)
    colunas = len(matriz)
    
    for i in range(linhas):
        for j in range(colunas):
            if i == j:
                if matriz[i][j] != 1:
                    return False
            else:
                if matriz[i][j] != 0:
                    return False
    
    return True


#Exercicio 22:
def f_determinanteMatriz(matriz):
    diagonal_principal = int()
    diagonal_secundaria = int()

    det = 0
    for linha in range(3):
        diagonal_principal = 1
        diagonal_secundaria = 1
        for coluna in range(3):
            diagonal_principal *= matriz[coluna][(linha + coluna) % 3]
            diagonal_secundaria *= matriz[coluna][(linha - coluna) % 3]
        det += diagonal_principal - diagonal_secundaria
            

    return det




#exercicio 23:

def f_matrizTransposta(M):
    for linha in range(len(M)):
        for coluna in range(linha):
            x = M[linha][coluna]
            y = M[coluna][linha]
            if (linha != coluna):
                M[linha][coluna] = y
                M[coluna][linha] = x
            
    return M
    

def f_matrizTriangularInferior(M):
    n = len(M)
    for linha in range(n):
        for coluna in range(linha+1, n):
            M[linha][coluna] = 0

    return M


#Exercicio 24:

def f_contarMovimentosValidos(tabuleiro, linha, coluna):
    movimentos_validos = 0
    movimentos_possiveis = [(linha - 2, coluna - 1), (linha - 2, coluna + 1),
                            (linha - 1, coluna - 2), (linha - 1, coluna + 2),
                            (linha + 1, coluna - 2), (linha + 1, coluna + 2),
                            (linha + 2, coluna - 1), (linha + 2, coluna + 1)]
        
    for movimento in movimentos_possiveis:
        l, c = movimento
        if 0 <= l < 8 and 0 <= c < 8 and tabuleiro[l][c] == 0:
            movimentos_validos += 1

    return movimentos_validos

def f_posicaoCavalo(tabuleiro):
    for i in range(8):
        for j in range(8):
            if tabuleiro[i][j] == 1:
                return i, j


def main():

    tabuleiro = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]

    linha_cavalo, coluna_cavalo = f_posicaoCavalo(tabuleiro)
    print(f_contarMovimentosValidos(tabuleiro, linha_cavalo, coluna_cavalo))


if __name__ == '__main__':
    main()
