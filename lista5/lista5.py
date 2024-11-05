# Questão 1
# A complexidade do método inverte_ordem é de O(n)
class list_node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next

    def inverte_ordem(head):
        current = head
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous

# Questão 2
def roman(num):
    algarism = ''
    parts = [0, 0, 0, 0]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    for i in range(3, -1, -1):
        parts[i] = num - (num % 10**i)
        num = num % 10**i
        for j in range(len(values)):
            while parts[i] >= values[j]:
                algarism += symbols[j]
                parts[i] -= values[j]
    return algarism
    
# Questão 3
# Item a
def potencia(number: float, exponent: int):
    if (exponent == 0 and number != 0):
        return 1
    if (exponent == 0 and number == 0):
        return
    resultado = 1
    if exponent > 0:
        for i in range(exponent):
            resultado *= number
    else:
        for i in range(abs(exponent)):
            resultado /= number
    return resultado

# Item b
def potencia_log_n(number: float, exponent: int):
    if (exponent == 0 and number != 0):
        return 1
    if (exponent == 0 and number == 0):
        return
    if exponent < 0:
        number = 1 / number
        exponent = -exponent
    result = 1
    while (exponent > 0):
        if (exponent % 2 == 1):
            result *= number
        number *= number
        exponent //= 2
    return result

# Questão 4
def busca(numbers):
    number = numbers[0]
    for i in range(1, len(numbers)):
        number = number ^ numbers[i]
    return number

# Questão 5
# A complexidade da função no pior caso está na ordem de O(n*m),
# onde n é a quantidade de entradas e m o tamanho da menor entrada.
def longest_common_prefix(words):
    shortest = words[0]
    for i in range(len(words)):
        if (len(words[i]) < len(shortest)):
            shortest = words[i]
    for i in range(len(shortest)):
        for j in range(len(words)):
            if (shortest[i] != words[j][i]):
                return shortest[:i]
    return shortest