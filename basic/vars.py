import decimal
from datetime import datetime

A = 4
a = 10
b = 5
c = a / b

# division always returns a floating point number
print(c)
print(type(c))

text = "# This is not a comment because it's inside quotes."
print(text)

x = 5 ** 2  # 5 squared
print(x)
x = 2 ** 7  # 2 to the power of 7
print(x)

print("# rounding")
tax = 12.5 / 100
price = 100.50
result = price * tax
print(result)
print(round(result, 2))

text = '"Isn\'t," they said.'
print(text)
text = "\"Yes,\" they said."
print(text)

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
text = 3 * 'un' + 'ium'
print(text)

# String literals next to each other are automatically concatenated
concat = 'Py' 'thon'
print(concat)

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

word = 'Python'
print(word[0])
print(word[5])
print(word[-1])  # last character
print(word[-2])  # second-last character
print(word[-6])

# In addition to indexing, slicing is also supported.
# While indexing is used to obtain individual characters,
# slicing allows you to obtain a substring:
print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[:2])   # character from the beginning to position 2 (excluded)
print(word[4:])   # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end
print(word[:2] + word[2:])
print(len(word))
print(word[4:42])  # 'on'
print(word[42:])   # empty

name = "Fred"
print(f"He said his name is {name!r} {len(name)}.")

width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f"result: {value:{width}.{precision}}")

today = datetime(year=2017, month=1, day=27)
print(f"{today:%B %d, %Y}")






