n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

cnt = [0] * (m+1)

for i in range(m):
    k,*tmp = list(map(int,input().split()))
    cnt[i+1] = k
    for c in tmp:
        graph[c].append(i+1)
        
b = list(map(int,input().split()))

answer = 0

hate = [False] * (n+1)

for i in b:
    hate[i] = True

for i in range(n+1):
    if hate[i]: continue
    for j in graph[i]:
        cnt[j] -= 1
        if cnt[j] == 0: answer += 1

for i in b:
    hate[i] = False
    for j in graph[i]:
        cnt[j] -= 1
        if cnt[j] == 0: answer += 1
    print(answer)