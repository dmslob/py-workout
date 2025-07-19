from collections import deque

queue = deque(["Eric", "John", "Michael"])
print(queue)

queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
print(queue)

print(queue.popleft())  # The first to arrive now leaves

print(queue.popleft())  # The second to arrive now leaves

print(queue.pop())  # The second to arrive now leaves

print(queue)