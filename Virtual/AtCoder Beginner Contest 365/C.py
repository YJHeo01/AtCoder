n,m = map(int,input().split())
array = list(map(int,input().split()))
if sum(array) <= m:
    print("infinite")
    exit(0)
max_x = 0
left, right = 0,m
while left <= right:
    x = (left+right) // 2
    tmp = 0
    for i in range(n):
        tmp += min(x,array[i])
    if tmp <= m:
        max_x = x
        left = x + 1
    else:
        right = x - 1
print(max_x)
