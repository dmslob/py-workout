basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print("'orange' in basket = ", 'orange' in basket)
print("'crabgrass' in basket = ", 'crabgrass' in basket)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print('unique letters in a: ', a)
print('unique letters in b: ', b)

print("letters in a but not in b: ", a - b)
print('letters in a or b or both: ', a | b)
print('letters in both a and b: ', a & b)
print('letters in a or b but not both', a ^ b)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)