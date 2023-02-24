"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

number_str = input('Input an integer: ')
try:
    number_int = int(number_str)
    if (number_int % 2 == 0):
        print(f'This is an even number')
    else:
        print(f'This is an odd number')
except:
    print(f'This is not an integer')

time_str = input('Input time in hours: ')
try:
    time_int = int(time_str)
    if (time_int >= 0 and time_int <= 11):
        print(f'Good morning')
    elif (time_int >= 12 and time_int <= 17):
        print(f'Good afternoon')
    else:
        print(f'Good Evening')
except:
    print(f'This is not a valid time in 24H format')

user_name = input('Input your name: ')
if (len(user_name) <= 4):
    print('Your name is small')
elif (len(user_name) == 5 or len(user_name) == 6):
    print('You got a medium name')
else:
    print('You got a big name')
