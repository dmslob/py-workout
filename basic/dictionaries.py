tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
print(tel.values())
print(tel)

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel))

print(sorted(tel))

print('guido' in tel)

print('jack' not in tel)

d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d)
d = dict(sape=4139, guido=4127, jack=4098)
print(d)

dc = {x: x**2 for x in (2, 4, 6)}
print(dc)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

for i, j in [(1, 2), (1, 3)]:
    print(i, j)

