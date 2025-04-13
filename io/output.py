import math
from datetime import date
import reprlib
import textwrap

print(reprlib.repr(set('supercalifragilisticexpialidocious')))

year = 2024
event = 'gig'
output = f'New event {event} {year}'
print(output)

print(str(1/7))
print(f'The value of pi is approximately {math.pi:.3f}.')

""" 
Passing an integer after the ':' will cause that field to be a minimum number of characters wide. 
This is useful for making columns line up.
"""
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

user = 'eric_idle'
member_since = date(1975, 7, 31)
delta = date.today() - member_since
print(f'{user=!s}  {delta.days=:,d}')


doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))

