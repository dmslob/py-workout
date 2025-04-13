import json

file_name = 'workfile.txt'
with open(file_name, 'w', encoding="utf-8") as f:
    value = ('the answer', 42)
    line = str(value)
    f.write(line)
f.closed

with open(file_name, 'r', encoding="utf-8") as f:
    # for line in f:
    #     print(line)
    read_data = f.read()
    print(read_data)
f.closed

x = [1, 'simple', 'list']
print(json.dumps(x))
y = {'key1': 'value1', 'key2': 'value2'}
print(json.dumps(y))


