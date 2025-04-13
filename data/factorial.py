def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


inp = 10
out = factorial(inp)
out_for = factorial_for(inp)
print(f'Factorial of {inp} is {out} using recursive function')
print(f'Factorial of {inp} is {out} using for loop')