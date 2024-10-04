import sys
import random
#Exercicio 1
def f_buscaSequencial(x,l):
    for i in range(len(l)):
        if x == l[i]:
            return True
    return False    

#Exercicio 2
def f_buscaSequencialV2(x,l):
    i = 0
    while i <= len(l):
        for nome,nome2, n in l:
            if n == x:
                return True
        i += 1
    return False

#Exercicio 3
def f_buscaBin(x,l):
    esquerda = 0
    direita = len(l) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if l[meio] == x:
            return True
        elif l[meio] < x:
            direita = meio - 1
        else:
            esquerda = meio + 1
    
    return False

#Exercicio 4
def f_buscaBinV2(x,l):
    esquerda = 0
    direita = len(l) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if l[meio] == x:
            return meio
        elif l[meio] > x:
            direita = meio - 1
        else:
            esquerda = meio + 1
    
    return -1


#Exercicio 5

#Exercicio 6:
def f_bubbleSort1(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

#Exercicio 7
def f_selectionSort(l):
    for i in range(len(l)):
        posMenor = i
        for j in range(i+1, len(l)):
            if l[posMenor] > l[j]:
                posMenor = j
        l[i], l[posMenor] = l[posMenor], l[i]

#Exercicio 8
def f_inserctionSort(l):
    for k in range(1, len(l)):
        elem = l[k]
        pos = k-1
        while pos >= 0 and l[pos] > elem:
            l[pos + 1] = l[pos]
            pos = pos - 1
        l[pos + 1] = elem 


#Exercicio 9
pontos = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(2000)]

def merge_sort(pontos):
    if len(pontos) > 1:
        meio = len(pontos) // 2
        esquerda = pontos[:meio]
        direita = pontos[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i][1] < direita[j][1]:
                pontos[k] = esquerda[i]
                i += 1
            else:
                pontos[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            pontos[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            pontos[k] = direita[j]
            j += 1
            k += 1

merge_sort(pontos)


print("A abscissa do último elemento é:", pontos[-1][0])



#Exercicio 10:
def distancia_ate_origem(ponto):
    return ponto[0]**2 + ponto[1]**2

def quick_sort(pontos):
    if len(pontos) <= 1:
        return pontos
    else:
        pivot = pontos[0]
        menor = [x for x in pontos[1:] if distancia_ate_origem(x) <= distancia_ate_origem(pivot)]
        maior = [x for x in pontos[1:] if distancia_ate_origem(x) > distancia_ate_origem(pivot)]
        return quick_sort(menor) + [pivot] + quick_sort(maior)

pontos_ordenados = quick_sort(pontos)

soma_abscissas = sum(ponto[0] for ponto in pontos_ordenados[:5])

print( soma_abscissas)


#Exercicio 11:

def main(args):


    l = [1,5,3,8,2,10]
    f_inserctionSort(l)
    print(l)
if __name__ == '__main__':
    sys.exit(main(sys.argv))