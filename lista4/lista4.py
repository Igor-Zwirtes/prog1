'''
TODO
Q2: 0,75
c) Não retornou Vector (-0,25)

Q3: 0,9
b) Não verifica divisão por 0 se ponto com mesmo x (-0,1)
'''

'''
Questão 1.
Item (a)
1
2

Item (b)
Value is bad

Item (c)
que massa!

Item (d)
[1, 2, 5, 4]

Questão 2.
Item (a)
Na linha 2 está escrito o método '__ints__', ao invés de '__init__',
além disso, a classe Vector está declarada com parênteses na linha 1, o que não é necessário

Item (b)
[]
[2.0, 1.0]

Item (c)
A saída não é a esperada, pois na linha 20 foi utilizado o valor de self nos dois elementos,
sendo que o correto seria 'new_vector[i] = self.values[i] + other_vector.values[i]'
'''

# Questão 3.
class Point:
    def __init__(self, x, y):
        self.abscissa = x
        self.ordered = y

# Item (a)
class Circle:
    def __init__(self, radius, point = Point(0, 0)):
        self.origin = point
        self.radius = radius

    def isInCircle(self, point):
        '''
        Verifica se a distância de um dado ponto até a origem do objeto circle é menor, igual ou maior ao comprimento do raio,
        Caso seja menor, o ponto está dentro do círculo, e a função retorna 1
        Caso seja maior, o ponto está fora do círculo, e a função retorna -1
        Caso seja igual, o ponto está sobre a circunferência, e a função retorna 0
        '''
        if ((((point.abscissa - self.origin.abscissa)**2 + (point.ordered - self.origin.ordered)**2)**0.5) < (self.radius)):
            return 1
        elif ((((point.abscissa - self.origin.abscissa)**2 + (point.ordered - self.origin.ordered)**2)**0.5) > (self.radius)):
            return -1
        else:
            return 0

# Item (b)
class Line_Segment:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2
        '''
        Verifica qual dos pontos dados é o início do segmento e qual é o final.
        '''
        if (point1.abscissa < point2.abscissa):
            self.start = point1.abscissa
            self.end = point2.abscissa
        else:
            self.start = point2.abscissa
            self.end = point1.abscissa
        self.inclination = (point2.ordered - point1.ordered) / (point2.abscissa - point1.abscissa)
        self.coeficient = (point1.ordered - (point1.abscissa * self.inclination))

    def isOnSegment(self, point):
        '''
        Verifica se o ponto dado está no intervalo fechado do segmento de linha.
        '''
        return ((point.ordered == (point.abscissa * self.inclination) + self.coeficient) and (point.abscissa >= self.start) and (point.abscissa <= self.end))

# Questão 4.
def lineIsInsideCircle(circle, line):
    '''
    Verifica se ambos os pontos do objeto line estão dentro do objeto círculo,
    Caso ao menos um dos pontos esteja sobre ou fora da circunferência, retorna False.
    '''
    return (circle.isInCircle(line.p1) == 1) and (circle.isInCircle(line.p2) == 1)

# Questão 5.
class Vector:
    def __init__(self, list):
        self.elements = list

    def dyadic_product(self, vector2):
        '''
        Retorna uma lista referente a matriz do produto tensorial dos dois vetores dados.
        '''
        product = []
        for i in range(len(self.elements)):
            product.append([])
            for j in range(len(vector2.elements)):
                product[i].append(self.elements[i] * vector2.elements[j])
        return product