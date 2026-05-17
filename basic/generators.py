def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

# Test
# given
word = 'test'
expected = ['t', 's', 'e', 't']

# when
w1 = list(reverse(word))
w2 = list(reversed(word))
w3 = list(word[i] for i in range(len(word) - 1, -1, -1))
w4 = list(i for i in reversed(word))

# then
assert w1 == expected
assert w2 == expected
assert w3 == expected
assert w4 == expected