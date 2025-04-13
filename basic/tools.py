from array import array
from collections import deque
# functions for manipulating sorted lists
import bisect
# functions for implementing heaps based on regular lists
from heapq import heapify, heappop, heappush

a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])

d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# rearrange the list into heap order
heapify(data)
print(data)
# add a new entry
heappush(data, -5)
print(data)
# fetch the three smallest entries
print([heappop(data) for i in range(3)])
