def f1(self, x, y):
    return min(x, x + y)


class Warehouse:
    f = f1
    purpose = 'storage'
    region = 'west'


w1 = Warehouse()
print(w1.f(10, 2))
print(w1.purpose, w1.region)

w2 = Warehouse()
print(w2.purpose, w2.region)
w2.region = 'east'
print(w2.purpose, w2.region)

print(w1.purpose, w1.region)


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def add_twice(self, x):
        self.add(x)
        self.add(x)


bag = Bag()
bag.add(1)
bag.add_twice(2)

print(bag.data)
print(bag.__class__)
print(type(bag))