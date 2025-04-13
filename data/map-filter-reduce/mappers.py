from typing import List


def upper(strs: List[str]) -> List[str]:
    return list(map(str.upper, strs))


pets = ['alfred', 'tabitha', 'william', 'arla']
print(upper(pets))  # ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']


def round_up(nums: List[float], start: int, end: int) -> List[float]:
    return list(map(round, nums, range(start, end)))


circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = round_up(circle_areas, 1, 7)
print(result)  # [3.6, 5.58, 4.009, 56.2424, 9.01344, 32.00013]
result = round_up(circle_areas, 1, 3)
print(result)  # [3.6, 5.58]

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]
results = list(zip(my_strings, my_numbers))
print(results)  # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
# same as:
results = list(map(lambda x, y: (x, y), my_strings, my_numbers))
print(results)
