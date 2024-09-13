n = int(input())

array = list(map(int,input().split()))

dp = [[0]*2 for _ in range(n)]

dp[0][1] = array[0]

for i in range(1,n):
    dp[i][0] = max(dp[i-1][0],dp[i-1][1]+array[i]*2)
    dp[i][1] = max(dp[i-1][1],dp[i-1][0]+array[i])

print(max(dp[n-1]))
