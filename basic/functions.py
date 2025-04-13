def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# Now call the function we just defined:
fib(2000)

x = 10


def test_vars():
    xx = x + 3
    return xx


print(test_vars())

i = 5


def f(arg=i):
    print(arg)


i = 6
f()
f(7)


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print(type(arguments))
    for arg in arguments:
        print(arg)
    print("-" * 40)
    print(type(keywords))
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def foo(name, /, **kwds):
    return 'name' in kwds
print(foo(1, **{'name': 2}))


def concat(*args, sep="/"):
    return sep.join(args)
print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

def my_function():
    """Do nothing, but document it.
    No, really, it doesn't do anything.
    """
    pass