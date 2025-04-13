from bitarray import bitarray

a = bitarray()         # create empty bitarray
print(a)

a.append(1)
print(a)

a.extend([1, 0])
print(a)

x = bitarray(2 ** 20)  # bitarray of length 1048576 (initialized to 0)
print(len(x))

lst = [1, 0, False, True, True]
a = bitarray(lst)      # initialize from iterable
print(a)

# Like lists, bitarray objects support slice assignment and deletion
a = bitarray(50)
a.setall(0)            # set all elements in a to 0
a[11:37:3] = 9 * bitarray('1')
print(a)


