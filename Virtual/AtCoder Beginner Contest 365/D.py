n = int(input())
s = list(input())

dp = [{'R':0,'P':0,'S':0} for _ in range(n+1)]

for i in range(n):
    for c in ['R','P','S']:
        for t in ['R','P','S']:
            if c == t: continue
            dp[i+1][c] = max(dp[i+1][c],dp[i][t])
    if s[i] == 'R':
        dp[i+1]['S'] = 0
        dp[i+1]['P'] += 1
    elif s[i] == 'S':
        dp[i+1]['P'] = 0
        dp[i+1]['R'] += 1
    else:
        dp[i+1]['S'] += 1
        dp[i+1]['R'] = 0

answer = 0

for i in ['R','P','S']:
    answer = max(dp[n][i],answer)

print(answer)
