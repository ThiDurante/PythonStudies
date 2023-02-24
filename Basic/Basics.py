print('line1')
print('line2')

# sep adds the selected character beetween elements
# end adds the selected character at the end of the line, any prevents line breaking
#  putting 2 prints together
print('Thiago', 'Durante', sep='-', end=' ')
print('Thiago', 'Durante')

print('012', '345', '678', sep='.', end='-')
print(90)

print('Reverse bar n \n breaks line')
# r at the start will prevent anything inside the string to run
print(r'Reverse bar n \n breaks lin')

# int is a integer positive or negative
# float is a real number (decimals) positive or negative

# type shows the class of the value
print(type('string'))  # string
print(type(10))  # int
print(type(10.53))  # float
print(type(10 == 10))  # bool
# type caching converts the value to what you specified
# theses values will return false
print(bool(''))
print(bool(0))
print(bool([]))


# arithmetic operators
# only works with ints and floats
# +, -, *, /
# * will also work as a repetition operator when used with strings
# the // rounds the division
# ** is exponential
# % rest of division
# () tells what should be done first

print(10 * 'a')

# variables, starts with a letter, can contain numbers, use _ to separate, lower case

name = 'Thiago'
age = 32
heigth = 1.87
can_drive = age > 18
weight = 90
imc = weight / heigth ** 2
print('Name: ', name)
print('age: ', age)
print('heigth: ', heigth)
print('can_drive: ', can_drive)
print('My imc is: ', imc)

# f strings enale you to use {} to put variables in it
# :.2f  will limit the number to have 2 decimals only
print(f'My name is {name} and I am {age} years old and my imc is: {imc:.2f}')
print('My name is {} and I am {} years old and my imc is: {:.2f}'.format(name, age, imc))
print('My name is {1} and I am {0} years old and my imc is: {2:.2f}'.format(
    name, age, imc))
