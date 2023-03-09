# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

import itertools


def zipper(list1, list2):
    result = []
    for i in range(min(len(list1), len(list2))):
        result.append((list1[i], list2[i]))
    return result


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1, l2))
print()
print()
print(list(zip(l1, l2)))
print()
print()
print(list(itertools.zip_longest(l1, l2, fillvalue='No City')))

l3 = [1, 2, 3, 4, 5, 6, 7]
l4 = [1, 2, 3, 4, 5]


def listSum(list1, list2):
    return [
        list1[i] + list2[i] for i in range(min(len(list1), len(list2)))
    ]


print()
print()
print()
print(listSum(l3, l4))


print()
print()
people = ['John', 'Beatrice', 'James', 'Otto', 'Jay', 'Liz']
print(list(itertools.combinations(people, 2)))
# combinations give us the combinations duuh, where order doesn't matter so no repetitions
# permutations gives us all combinations where order matter

t_shirts = [
    ['black', 'white'],
    ['small', 'medium', 'large'],
    ['male', 'female']
]
print()
print()

print(list(itertools.product(t_shirts)))
# this will only separate the lists in tuples, but if you use *
print()
print()
print(*list(itertools.product(*t_shirts)), sep='\n')
# this crosses all elements creating diferent products with all the properties in tuples
