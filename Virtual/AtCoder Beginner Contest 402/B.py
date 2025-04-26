from collections import deque

q = int(input())

queue = deque([])

for _ in range(q):
    tmp = list(input().split())
    if tmp[0] == '1':
        queue.append(tmp[1])
    else:
        print(queue.popleft())
