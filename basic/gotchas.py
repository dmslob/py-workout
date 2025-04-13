# Python’s default arguments are evaluated once when the function is defined,
# not each time the function is called
# This means that if you use a mutable default argument and mutate it,
# you will and have mutated that object for all future calls to the function as well.
def append_to(element, to=[]):
    to.append(element)
    return to

my_list = append_to(12)
print(my_list)

my_other_list = append_to(42)
print(my_other_list)


def create_multipliers():
    return [lambda x: i * x for i in range(5)]
# same
def create_multipliers1():
    multipliers = []
    for i in range(5):
        def multiplier(x):
            return i * x
        multipliers.append(multiplier)
    return multipliers

for multiplier in create_multipliers():
    print(multiplier(2))


def create_multipliers():
    return [lambda x, i=i: i * x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2))

