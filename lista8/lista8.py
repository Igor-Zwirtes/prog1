# Questão 1
def merge_lists(list1, list2):
    new_list = []
    n, m = 0, 0
    # Verifica qual o maior elemento entre os atuais indíces da respectiva lista até que uma delas seja percorrida completamente
    while n < len(list1) and m < len(list2):
        if list1[n] > list2[m]:
            new_list.append(list1[n])
            n += 1
        else:
            new_list.append(list2[m])
            m += 1

    # Verifica qual lista foi percorrida até o final e adiciona os elementos restantes da outra lista
    if n == len(list1):
        for i in range(m, len(list2)):
            new_list.append(list2[i])
    else:
        for i in range(n, len(list1)):
            new_list.append(list1[i])
    return new_list

# Questão 2
def shop(n, K, N):
    total = 0
    buyed = []
    # Para cada elemento da lista N, verifica se o tipo atual está entre os últimos k itens comprados
    # Enquanto K for maior que a quantidade de itens comprados, verifica todos os itens já comprados
    for d in range(n):
        buy = True
        for i in range(min(K, len(buyed))):
            if N[d] == buyed[-i-1]:
                buy = False
        if buy:
            total += 1
            buyed.append(N[d])
    return total

# Questão 3
def is_valid(string):
    parentesis = 0
    # Para cada '(', adiciona 1 à contagem de parêntesis abertos,
    # Caso a contagem seja negativa em algum momento, um parêntesis foi fechado sem ter um '(' correspondente, então não é válido
    # Ao final, verifica se sobrou algum parêntesis aberto, já que é necessário que todos sejam fechados
    for i in range(len(string)):
        if parentesis < 0:
            return False
        if string[i] == '(':
            parentesis += 1
        if string[i] == ')':
            parentesis -= 1
    return parentesis == 0