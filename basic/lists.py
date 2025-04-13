import math

squares = [1, 4, 9, 16, 25]
print(squares[:3])

print(squares.extend([2, 5, 12]))
print(squares.pop())
print(squares.index(4, 0, 3))


# concatenation
newSquares = squares + [36, 49, 64, 81, 100]
print(newSquares)
newSquares.append(121)
print(newSquares)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)

# now remove them
letters[2:5] = []
print(letters)
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

# it is possible to nest lists (create lists containing other lists), for example:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x[0][1])

squares = []
for x in range(10):
    squares.append(x**2)
print(squares, x)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

xy = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(xy)


a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

del a

s = 'abc$ # 321 '
print(f'List of Characters ={list(s)}')

List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Display sliced list
print(List[3:9:2])

ls = ['1', '2']
for i, v in enumerate(ls):
    print(i, v)

# To loop over two or more sequences at the same time,
# the entries can be paired with the zip() function
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# To loop over a sequence in reverse
for i in reversed(range(1, 10, 2)):
    print(i)

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

cars = []
if cars:
    print(cars)
else:
    print('no cars')


sts = ['Paid', 'Overdue', 'Paid']
result = map(lambda x: 0 if x == 'Paid' else 1, sts)
print(list(result))

print(max([1.90, 2.89]))