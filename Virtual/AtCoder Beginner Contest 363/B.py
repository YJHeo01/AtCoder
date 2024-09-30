answer = 0

n,t,p = map(int,input().split())
array = list(map(int,input().split()))

while True:
    tmp = 0
    for i in range(n):
        if array[i] >= t:
            tmp += 1
        array[i] += 1
    if tmp >= p: break
    answer += 1

print(answer)
