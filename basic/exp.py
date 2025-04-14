vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
doubled = [x * 2 for x in vec]
print(doubled)

# filter the list to exclude negative numbers
with_no_negatives = [x for x in vec if x >= 0]
print(with_no_negatives)

# apply a function to all the elements
abs = [abs(x) for x in vec]
print(abs)

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
stripped = [weapon.strip() for weapon in freshfruit]
print(stripped)

# create a list of 2-tuples like (number, square)
tuples = [(x, x ** 2) for x in range(6)]
print(tuples)

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
listcomp = [num for elem in vec for num in elem]
print(listcomp)

mtr = list(zip([1, 2, 3], [4, 5, 6]))
print(mtr)
