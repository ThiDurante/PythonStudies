# create functios that double, triple and quadruple the value passed as a paramter

# def double(number):
#     return number * 2


# def triple(number):
#     return number * 3


# def quadruple(number):
#     return number * 4


# duplicate = double(4)
# print(duplicate)

# triplicate = triple(4)
# print(triplicate)

# quadruplicate = quadruple(4)
# print(quadruplicate)

def create_multiplier(multiplier):
    def multiply(number):
        return number * multiplier
    return multiply


duplicate = create_multiplier(2)
triplicate = create_multiplier(3)
quadruplicate = create_multiplier(4)


print(duplicate(3))
print(triplicate(3))
print(quadruplicate(3))
