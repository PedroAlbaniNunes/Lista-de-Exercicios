#Exercicio 1:
def f_fatRecurssivo(n):
    if n == 0:
        return 1
    else:
        return n * f_fatRecurssivo(n-1)
        

#Exercicio 2:
def f_somarListaRecurssivo(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + f_somarListaRecurssivo(l[1:])

#Exercicio 3:
def f_fibonnachiIterativo(n):
    l = list()

    if n == 1:
        l = [1]
    elif n == 2:
        l = [1,1]
    else:
        l = [1,1]

    for i in range(n-2):
        l.append(l[-1]+l[-2])
    return l[-1]

def f_fibonnachiRecursivo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f_fibonnachiRecursivo(n-1) + f_fibonnachiRecursivo(n-2)

#A versão recurssiva demora consideralvemente mais tempo do que a versão iterativa, pois ela depende de refazr o calculo todas as vezes.

#Exercicio 4:
def f_expoRecurssivo(x,n):
    if n == 1:
        return x
    elif n == 0:
        return 1
    else:
        return x * f_expoRecurssivo(x,n-1)

#Exercicio 5:
#definir o maior entre um e outro
def f_maior(x,y):
    if x > y:
        return x
    else:
        return y
    
#definir o maior da lista
def f_maiorElementoListaRecurssivo(l):
    if len(l) == 1:
        return l[0]
    else:
        return f_maior(l[0], f_maiorElementoListaRecurssivo(l[1:]))

        

#Exercicio 6:
def f_maxDivComum(x,y):
    if x % y == 0:
        return y
    else:
        return f_maxDivComum(y, x % y)
    
#Exercicio 7:

def f_contrario(x):
    if x // 10 == 0:
        print(x)
    else:
        print(x%10, end='')
        f_contrario(x//10)

#Exercicio 8:
def f_torreHanoi(n, origem, destino, auxiliar):

    if n == 1:
        print(origem , '->', destino)
    else:
        f_torreHanoi(n-1, origem, auxiliar, destino)
        print(origem, '->', destino)
        f_torreHanoi(n-1, auxiliar, destino, origem)
         

#Exercicio 9:
def f_troca(l, i, j):
    aux = l[i]
    l[i] = l[j]
    l[j] = aux

def f_permutacao(l, pos=0):
    if pos == len(l) - 1:
        print(l)
    else:
        for i in range(pos, len(l)):
            f_troca(l, pos, i)
            f_permutacao(l, pos+1)
            f_troca(l, pos, i)


#Exercicio 10:
def f_eucliadiana(m,n):
    _, x1, y1 = m
    _, x2, y2 = n

    return ((y1-x1)**2 + (y2-x2)**2)**0.5


    

def main():

    l = [1,2,3,4]
    f_permutacao(l)
if __name__ == '__main__':
    main()