import dis


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[0])
print(pairs)

calc = lambda n: n * n
print(calc(10))

add_one = lambda x: x + 1
print(add_one(2))

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))

plus = lambda x, y: x + y
print(plus(1, 3))

high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))
print(high_ord_func(2, lambda x: x + 3))

add = lambda x, y: x + y
print(type(add))

dis.dis(add)


def full_name(first: str, last: str) -> str:
    return f'{first.title()} {last.title()}'


print(full_name("Bob", "Dred"))


def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)

    return wraps


@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")


print(decorated_function("Python"))


# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap


# Applying decorator to a function
@trace
def add_two(x):
    return x + 2


# Calling the decorated function
add_two(3)

# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))
