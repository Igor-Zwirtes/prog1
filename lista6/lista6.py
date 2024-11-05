# Quastão 1
def search_insert(numbers, number):
    start = 0
    end = len(numbers) - 1
    while (start <= end):
        i = (start + end) // 2
        if (numbers[i] == number):
            return i
        if (numbers[i] > number):
            end = i - 1
        else:
            start = i + 1
    return start

# Questão 2
# A complexidade é de O(n²)
def pascal_triangle(level):
    triangle = []
    for i in range(level):
        triangle.append([])
        for j in range(i + 1):
            if (j == 0 or j == i):
                triangle[i].append(1)
            else:
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
    return triangle

# Questão 3
class List_Node:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next


class Linked_List:
    # Item (a)
    def __init__(self, head = None):
        self.head = head
        if (self.head != None):
            self.length = 1
        else:
            self.length = 0
        N = self.head
        while (N != None):
            self.length += 1
            N = N.next

    # Item (b)
    def delete_node(self, value):
        if (self.length == 0):
            return
        while (self.head.val == value):
            self.head = self.head.next
            self.length -= 1
        if self.length == 0:
            return
        N = self.head
        while (N.next != None):
            if (N.next.val == value):
                N.next = N.next.next
                self.length -= 1
                continue
            N = N.next

    # Item (c)
    def __add__(self, list2):
        N = self.head
        M = list2.head
        while (N.next != None):
            N = N.next
        while (M != None):
            self.length += 1
            N.next = M
            M = M.next
            N = M

# Questão 4
def polynomial_to_dict(poly):
    dict = {}
    for i in range(len(poly)):
        if (poly[i] == 'x'):
            if (i > 1):
                if (poly[i+1] == '+' or poly[i+1] == '-'):
                    if (poly[i-2] == '+'):
                        dict[1] = int(poly[i-1])
                    elif (poly[i-2] == '-'):
                        dict[1] = int(poly[i-1]) * (-1)
                elif (poly[i-2] == '+'):
                    dict[int(poly[i+2])] = int(poly[i-1])
                elif (poly[i-2] == '-'):
                    dict[int(poly[i+2])] = int(poly[i-1]) * (-1)
                elif (poly[i-1] == '+'):
                    dict[int(poly[i+2])] = 1
                elif (poly[i-1] == '-'):
                    dict[int(poly[i+2])] = -1
            elif (i == 1):
                dict[int(poly[i+2])] = int(poly[i-1])
            elif (i == 0):
                dict[int(poly[i+2])] = 1
        elif (i == len(poly) - 1 and (poly[i-1] == '+' or poly[i-1] == '-')):
            if (poly[i-1] == '+'):
                dict[0] = int(poly[i])
            elif (poly[i-1] == '-'):
                dict[0] = int(poly[i]) * (-1)
    return dict

# Questão 5
def dict_to_polynomial(dict):
    poly = ''
    first = True
    for i in sorted(dict, reverse= True):
        if (i == 0):
            if (dict[i] >= 0):
                if (first == False):
                    poly += f'+{dict[i]}'
                else:
                    poly += f'{dict[i]}'
            else:
                poly += f'{dict[i]}'
        elif (i == 1):
            if (dict[i] >= 0):
                if (first == False):
                    if (dict[i] != 1):
                        poly += f'+{dict[i]}x'
                    else:
                        poly += '+x'
                else:
                    if (dict[i] != 1):
                        poly += f'{dict[i]}x'
                    else:
                        poly += 'x'
                    first = False
            else:
                if (dict[i] != -1):
                        poly += f'{dict[i]}x'
                else:
                    poly += '-x'
                first = False
        elif (dict[i] >= 0):
            if (first == False):
                if (dict[i] != 1):
                    poly += f'+{dict[i]}x^{i}'
                else:
                    poly += f'+x^{i}'
            else:
                if (dict[i] != 0):
                    poly += f'{dict[i]}x^{i}'
                else: poly += f'x^{i}'
                first = False
        elif (dict[i] < 0):
            if (dict[i] != -1):
                poly += f'{dict[i]}x^{i}'
            else:
                poly += f'-x^{i}'
            first = False
    return poly