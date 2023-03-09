def fabrica_de_decoradores(a=None, b=None, c=None):

    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


# print(soma(15, 5))

decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)
subtracao = decoradora(lambda x, y: x - y)

# dez_mais_cinco = soma(25, 5)
# dez_vezes_cinco = multiplica(10, 5)
# print(dez_mais_cinco)
# print(dez_vezes_cinco)

# lambda = nome
# x, y = args
# : = sinaliza fim de arg
# x * y = retorno

# lambda x, y: x * y
