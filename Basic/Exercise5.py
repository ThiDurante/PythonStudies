"""
Build a CPF (brazilian document) validator
A CPF has 12 numbers, it is validated by the last 2 digits
The first digit is equal to a sum of a regressive multiplication, starting at 10, with all the previous numbers so,
746.828.890-80 is a CPF

 10  9  8  7  6  5  4  3  2  times:
 7   4  6  8  2  4  8  9  0 
 70  36 48 56 12 20 32 27 0 = total 301
 
 then we get that result and multiply by 10 = 3010
 then we get the rest of the division by 11 so, 3010 % 11 = 7
 If the number is bigger than 9, CPF must have 0 on the first of the last 2 digits
 If its smaller than 9, like 7, that number will be the first of the last 2 digits

  The second digit has the same method but multiplication starts at 11 and includes the digit that was generated above
"""
import re
import sys
import random


while True:
    # asking user what he wants to do

    operation = input(
        'Do you want to [c]reate a CPF, check if one is [v]alid or [e]xit: ')
    user_CPF = 'v'

    # asking for the CPF
    if operation == 'v':
        user_CPF = input('Input a cpf like 746.824.890-70: ')
    # cleanning the input
        clean_user_CPF = re.sub(r'[^0-9]', '', user_CPF)
    # checking if data is repetitive numbers, something like 11111111111 will be validated by the algorithm
        repetitive_numbers_validator = clean_user_CPF == clean_user_CPF[0] * len(
            clean_user_CPF)
        if repetitive_numbers_validator:
            print('Repetitive numbers are not allowed')
            return continue

    # separating the digits on strings

    last_two_digits = clean_user_CPF[9:] if operation == 'v' else ''
    nine_digits = clean_user_CPF[:9] if operation == 'v' else ''

    if operation == 'c':
        for i in range(9):
            nine_digits += str(random.randint(0, 9))

    # last_two_digits = ''.join(user_CPF.split('.')).split('-')[1]
    # nine_digits = ''.join(user_CPF.split('.')).split('-')[0]

    # calculating the first digit
    # making the multiplication

    regressive_multiplication = 0
    multiplicator = 10

    for number in nine_digits:
        regressive_multiplication += int(number) * multiplicator
        multiplicator -= 1
        if multiplicator < 2:
            multiplicator = 10

    # now we multiply the result by 10 and get the rest of the division by 11

    first_digit = (regressive_multiplication * 10) % 11

    # checking if its bigger than 9

    first_digit if first_digit <= 9 else 0

    CPF_with_first_digit = nine_digits + str(first_digit)

    regressive_multiplication2 = 0
    multiplicator2 = 11

    for number in CPF_with_first_digit:
        regressive_multiplication2 += int(number) * multiplicator2
        multiplicator2 -= 1
        if multiplicator2 < 2:
            multiplicator2 = 11

    second_digit = (regressive_multiplication2 * 10) % 11

    second_digit if second_digit <= 9 else 0

    if operation == 'v':
        user_CPF_formated = nine_digits + last_two_digits
        full_CPF = CPF_with_first_digit + str(second_digit)

        if (user_CPF_formated == full_CPF):
            print(f'{user_CPF} is a valid CPF')
        else:
            print(f'{user_CPF} is not a valid CPF')
    elif operation == 'c':
        random_CPF = nine_digits + str(first_digit) + str(second_digit)
        print(f'Here is your randomly generated CPF: {random_CPF}')
    elif operation == 'e':
        print('Thanks for using my CPF generator/validator')
        sys.exit()
    else:
        print('This is not a valid operation')
