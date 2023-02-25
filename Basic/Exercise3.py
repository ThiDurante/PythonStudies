"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

secret_word = 'cheese'
correct_letters = ''
trys = 0
game_over = True

while game_over:
    user_letter = input('Insert a letter: ')
    if (len(user_letter) > 1):
        print('Type only one letter')
        continue
    trys += 1
    if user_letter in secret_word:
        correct_letters += user_letter
    answer = ''
    for letter in secret_word:
        if letter in correct_letters:
            answer += letter
        else:
            answer += '*'
    print(f'Word: {answer}')
    if answer == secret_word:
        os.system('cls')
        print(f'Congrats! the word was {secret_word}')
        print(f'You tried {trys} times')
        trys = 0
        answer = ''
        correct_letters = ''
