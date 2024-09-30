import sys

input = sys.stdin.readline

n,q = map(int,input().split())

s = list(input())
answer = 0

visited = [False] * n

for i in range(2,n):
    idx = i - 2
    if s[i-2] == 'A' and s[i-1] == 'B' and s[i] == 'C':
        visited[idx] = True
        answer += 1

for _ in range(q):
    x,c = input().split()
    i = int(x) - 1
    s[i] = c
    for k in range(3):
        new_i = i + k
        idx = new_i - 2
        if idx < 0: continue
        if s[new_i-2] == 'A' and s[new_i-1] == 'B' and s[new_i] == 'C':
            if visited[idx] == True: continue
            answer += 1
            visited[idx] = True
        else:
            if visited[idx] == False: continue
            answer -= 1
            visited[idx] = False
    print(answer)
