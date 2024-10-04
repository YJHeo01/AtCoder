n,k = map(int,input().split())
array = sorted(list(map(int,input().split())))
answer = int(1e9)
for i in range(k+1):
    answer = min(answer,array[n-k+i-1]-array[i])
print(answer)
