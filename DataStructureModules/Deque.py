from collections import deque


L = [1, 2, 3, 4, 5, 6]


q = deque(L)

q.append(7)

print(q)

q.appendleft(9)
print(q)

q.pop()
print(q)

q.popleft()
print(q)

q.extend([11, 12, 13])
print(q)

q.extendleft([50, 60, 70])
print(q)


q.rotate(2)
print(q)

