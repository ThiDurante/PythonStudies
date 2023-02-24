"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

name = input('Type your name: ')
age = input('Type your age: ')
if name and age:
    print(f'Your name is {name} and your age is {age}')
    print(f'Your name has {len(name)} letters')
    if ' ' in name:
        print(f'Your name has spaces')
    else:
        print(f'Your name doesn\'t have spaces')
    print(f'The first letter of your name is {name[0]}')
    print(f'The last letter of your name is {name[len(name) - 1]}')
else:
    print(f'You need to provide both name and age!')
