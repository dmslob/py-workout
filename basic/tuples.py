t = 12345, 54321, 'hello!'
print(t)
print(t[0])

# Tuples are immutable:
# t[0] = 88888

x, y, z = t
print(x, y, z)

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(singleton))
print(singleton)

