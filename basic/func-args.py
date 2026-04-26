def add(a, b, *args):
    return sum((a, b)) + sum(args)


print(add(1, 2, 3, 4))


def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)


magic(1, 2, key="word", key2="word2")
magic(3, 4)


def other_way_magic(x, y, z):
    return x + y + z


x_y_list = [1, 2]
z_dict = {"z": 3}
print(other_way_magic(*x_y_list, **z_dict))  # output: 6


def add(x, y):
    return x + y

def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(add)
print(g(1, 2))  # 6
