from functools import reduce

custom_sum = lambda first, second: first + second

numbers = [3, 4, 6, 9, 34, 12]
result = reduce(custom_sum, numbers)
print(result)  # 68
result = reduce(custom_sum, numbers, 10)  # with initial value 10
print(result)  # 78

# Map Filter Reduce example
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 9, 23, 5]

# Use map to print the square of each number rounded to three decimal places
map_result = list(map(lambda x: round(x ** 2, 3), my_floats))

# Use filter to print only the names that are less than or equal to seven letters
filter_result = list(filter(lambda name: len(name) <= 7, my_names))

# Use reduce to print the product of these numbers
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)  # [18.922, 37.088, 10.562, 95.453, 4.666, 78.854, 21.068]
print(filter_result)  # ['olumide', 'josiah', 'omoseun']
print(reduce_result)  # 24840
