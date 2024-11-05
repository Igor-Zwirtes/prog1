'''
Questão 1
Item (a)
Linha 10: mcc1 = sum2list([1], [3,5,6])

Item (b)
Não é um bom nome.
def product_of_two_lists(l1, l2):
    r = []
    for n1 in l1:
        c = []
        # adds the elements from the temporary list c to the list r
        r.append(c)
        for n2 in l2:
            # multiply each element of the first list by all elements of the second list individually
            c.append(n1*n2)
    return r
'''

# Questão 2
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if (nums[i] + nums[j] == target):
                return[i, j]
            
# Questão 3
def average(nums):
    total_sum = 0
    for i in range(len(nums)):
        total_sum += nums[i]
    return (total_sum / len(nums))

# Questão 4
def minus_num(nums, subtract):
    for i in range(len(nums)):
        nums[i] -= subtract
    return nums

# Questão 5
def std_deviation(nums):
    nlist = minus_num(nums, average(nums))
    total_sum = 0
    for i in range(len(nums)):
        total_sum += (nlist[i])**2
    return (total_sum / len(nums))**0.5