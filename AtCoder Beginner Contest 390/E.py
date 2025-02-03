import sys

input = sys.stdin.readline

n,x = map(int,input().split())

vitamin = [[] for _ in range(4)]

for _ in range(n):
    v,a,c = map(int,input().split())
    vitamin[v].append((a,c))

dp = [[-1] * (x+1) for _ in range(4)]

for i in range(1,4):
    dp[i][0] = 0
    for a,c in vitamin[i]:
        for target in range(x,-1,-1):
            last = target - c
            if last < 0: break
            if dp[i][last] == -1: continue
            dp[i][target] = max(dp[i][target],dp[i][last]+a)

for i in range(1,4):
    for j in range(x):
        dp[i][j+1] = max(dp[i][j],dp[i][j+1])

answer = 0

for a in range(x+1):
    for b in range(x-a+1):
        c = x - a - b
        answer = max(answer,min(dp[1][a],dp[2][b],dp[3][c]))

print(answer)
