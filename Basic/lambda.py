def execute(func, *args):
    return func(*args)


def sumTest(x, y):
    return x + y


print(execute(lambda x, y: x + y, 2, 3))


def create_multiplier(multiplier):
    def multiply(number):
        return number * multiplier
    return multiply


# better
duplicate1 = create_multiplier(2)
# do not use this, just for undertanding
duplicate2 = execute(
    lambda m: lambda n: n*m,
    2
)

print(duplicate1(2))
print(duplicate2(2))

print(
    execute(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)
