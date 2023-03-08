# # Exercício - Adiando execução de funções
# def soma(sumBy):
#     def sum(number):
#         return number + sumBy
#     return sum


# def multiplier(multiplier):
#     def multiply(number):
#         return number * multiplier
#     return multiply


# def criar_funcao(funcao, *args):
#     return funcao(*args)

def soma(x, y):
    return x + y


def multiplier(x, y):
    return x * y


def create_func(func, x):
    def insideFunc(y):
        return func(x, y)
    return insideFunc


soma_com_cinco = create_func(soma, 5)
multiplica_por_dez = create_func(multiplier, 10)

print(soma_com_cinco(5))
print(multiplica_por_dez(5))


def concatenator(initial_string):
    final_value = initial_string

    def to_concatenate(value=''):
        nonlocal final_value
        final_value += value
        return final_value
    return to_concatenate


initialA = concatenator('A ')
initialA('happy ')
initialA('dog')
initialA('!')
print(initialA())
