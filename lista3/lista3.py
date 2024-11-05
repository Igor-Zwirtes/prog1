'''
Questão 1
Item (a)
11
21
13
Ola
casa
carro
pé

Item (b)
11
True
13
Ola

Item (c)
pé
Ola
11

Item (d)
[11,22,33,44]
[1,2,3,4]
['ola','tchau']
'''

# Questão 2
def isPalindrome(word):
    if (len(word) % 2 == 0):
        for i in range(len(word)):
            if (word[i] != word[-(i+1)]):
                return False
    else:
        for i in range(len(word)//2):
            if (word[i] != word[-(i+1)]):
                return False
    return True

# Questão 3
def get_vogals(text):
    vogals_list = []
    vogals = ['a','e','i','o','u']
    for i in range(len(text)):
        if (text[i].lower() in vogals):
            if (text[i].lower() not in vogals_list):
                vogals_list.append(text[i].lower())
    vogals_list.sort()
    return vogals_list

# Questão 4
def encoder(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    index = 0
    for i in range(len(text)):
        index.find(text[i])
        if (index != -1):
            if (index > 0):
                encrypted += alphabet[index-1]
            else:
                encrypted += alphabet[25]
        else:
            encrypted += text[i]
    return encrypted

# Questão 5
def isAnagram(word1, word2):
    letters = []
    for i in range(len(word1)):
        letters.append(word1[i])
    for i in range(len(word2)):
        if (word2[i] not in letters):
            return False
        else:
            for j in range(len(letters)):
                if (word2[i] == letters[j]):
                    letters.remove(word2[i])
                    break
    return (letters == [])