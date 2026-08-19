# q = []
# q.append(1)
# q.append(2)
# q.append(3)
# print(q)
# q.pop(0)
# print(q)
# print(q[0])

from collections import deque
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.popleft() 
print(q)