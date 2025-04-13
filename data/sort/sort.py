persons = ['Chris', 'Amber', 'David', 'El-dorado', 'Brad', 'Folake']

sortedPersons = sorted(persons)
print(persons)
print(f'Sorted persons {sortedPersons} by sorted() function')
persons.sort()
print(f'Sorted persons {persons} by persons.sort() function')
print(persons == sortedPersons)

numbers = (14, 3, 1, 4, 2, 9, 8, 10, 13, 12)
sortedNumbers = sorted(numbers)
print(sortedNumbers)

# If you use the sorted() method with a dictionary,
# only the keys will be returned and as usual, it will be in a list:
my_dict = {'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
sortedDict = sorted(my_dict)
print(f'Sorted list of keys {sortedDict}')

footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125, 'Aaron': 115}
sorted_footballers_by_goals = sorted(footballers_goals.items(),
                                     key=lambda x: x[1], reverse=True)  # 0 - by keys, 1 - by values
print(f'Result of sorting {sorted_footballers_by_goals}')
converted_dict = dict(sorted_footballers_by_goals)
print(f'Result converted to dict {converted_dict}')
