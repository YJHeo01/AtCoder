n,m = map(int,input().split())
a = list(map(int,input().split()))
for _ in range(n):
    tmp = list(map(int,input().split()))
    for i in range(m):
        a[i] -= tmp[i]
answer = "Yes"
for i in range(m):
    if a[i] > 0: answer = "No"
print(answer)
