cht = "\t\tHappy new year"
print(cht)
for leaf in [*range(10)] + [2]:
    print(f'{"x" * (leaf * 2 + 1):^30}')