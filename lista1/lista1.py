'''
Questão 1
Item (a)
10
11
1
13
Ola
casa
carro
pé

Item (b)
0
1
2
3
4
5
6
7

Item (c)
11
OLA
13
Ola
casa
'''

# Questão 2
def sum_cumulative(myList):
    nlist = myList[:]
    for i in range(len(myList)):
        for j in range(i):
            nlist[i] += myList[j]
    return nlist

# Questão 3
def nested_sum(listOfLists):
    total_sum = 0
    for i in range(len(listOfLists)):
        for j in range(len(listOfLists[i])):
            total_sum += listOfLists[i][j]
    return total_sum

# Questão 4
def relatively_prime(x, y):
    if (x > y):
        if (x % y == 0):
            return False
        else:
            return True
        #TODO Precisa comprar MDC
    elif (x < y):
        if (y % x == 0):
            return False
        else:
            return True
    else:
        return False
    
# Questão 5
def before_half(x):
    i = (x // 2) + 1
    while (i <= x):
        print(i)
        i += 1
#TODO Faltou tratar negativos, lista em ordem decrescente