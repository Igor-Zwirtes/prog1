# Questão 1
import csv
import turtle

def make_file(start, end, step, filename):
    results = {}
    i = start
    while (i <= end):
        # Salva os resultados do polinômio no intervalo em um dicionário onde a chave é o valor de x e o elemento é o valor de y
        results[round(i, 10)] = i**8 - 3*i**4 + 2*i**3 - 2*i**2 - i + 2
        i += step

    with open(filename, mode = 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(['X', 'Y'])
        # Salva cada par de valores x e y em uma linha distinta em um arquivo .csv
        for x, y in results.items():
            writer.writerow([x, y])

def plot_graph(filename):
    # Desenha os eixos do gráfico
    turtle.Screen().setworldcoordinates(-2, -6, 2, 14)
    turtle.tracer(0, 0)
    plotter = turtle.Turtle()
    plotter.speed(0)
    plotter.penup()
    plotter.goto(-2, 0)
    plotter.pendown()
    plotter.goto(2, 0)
    plotter.penup()
    plotter.goto(0, -6)
    plotter.pendown()
    plotter.goto(0, 14)
    plotter.penup()
    with open(filename, mode = 'r') as file:
        reader = csv.DictReader(file)
        # Faz um ponto no gráfico para cada ponto do polinômio salvo no arquivo
        for row in reader:
            x = float(row['X'])
            y = float(row['Y'])
            plotter.goto(x, y)
            plotter.dot(3, 'blue')
    plotter.hideturtle()
    turtle.done()

make_file(-1.5, 1.5, 1/500, 'points.csv')
plot_graph('points.csv')

# Questão 2
def merge_intervals(input):
    # Ordena os intervalos em ordem crescente em relação ao início do intervalo
    input.sort(key = lambda x: x[0])
    output = [input[0]]
    for i in input:
        # Se o início do intervalo atual estiver dentro do intervalo anterior, altera o final entre o maior valor entre ambos intervalos
        # Caso contrário, adiciona o intervalo atual à lista
        last_merged = output[-1]
        if i[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], i[1])
        else:
            output.append(i)
    return output

# Questão 3
def missing_int(numbers):
    start = 0
    end = len(numbers)
    while (end > start):
        i = (start + end) // 2
        # Verifica se a quantidade de elementos no invervalo analisado é igual a diferença entre os valores
        # Caso seja igual, o primeiro elemento que falta estará depois no índice atual
        # Caso contrário, está antes
        if (numbers[i] - numbers[start] == (i - start)):
            start = i + 1
        else:
            end = i - 1
    return numbers[start] + 1

# Questão 4
class List_Node:
    def __init__(self, value = '', next = None):
        self.val = value
        self.next = next

class Linked_List:
    def __init__(self, head = None):
        self.head = head

    def __add__(self, list2):
        N = self.head
        M = list2.head
        while (N.next != None):
            N = N.next
        while (M != None):
            N.next = M
            M = M.next
            N = M

def isPalindrome(head):
    # Transforma a lista em uma string
    word = ''
    N = head.head
    while N != None:
        word += N.val
        N = N.next

    # Caso o comprimento da string seja ímpar, verfica cada elemento com o de índice oposto
    if (len(word) % 2 == 0):
        for i in range(len(word)):
            if (word[i] != word[-(i+1)]):
                return False
            
    # Caso o comprimento seja ímpar, verifica apenas até o elemento mediano da string
    else:
        for i in range(len(word)//2):
            if (word[i] != word[-(i+1)]):
                return False
    return True