def add(a, b, *args):
    return sum((a, b)) + sum(args)


print(add(1, 2, 3, 4))