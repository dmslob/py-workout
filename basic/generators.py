def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)

# sum of squares
sum_of_squares = sum(i * i for i in range(10))
print(sum_of_squares)

data = 'golf'
for i in reversed([1, 3]):
    print(i)
reversedList = list(data[i] for i in range(len(data) - 1, -1, -1))
print(reversedList)
