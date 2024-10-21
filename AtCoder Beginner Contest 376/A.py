from collections import deque

n,c = map(int,input().split())
queue = deque(list(map(int,input().split())))
last_time = -1001
answer = 0
while queue:
    t = queue.popleft()
    if t >= last_time + c:
        answer += 1
        last_time = t
print(answer)
