n = int(input())

array = list(map(int,input().split()))

tmp = []

for i in range(n):
    tmp.append((array[i],i))

tmp.sort()

print(tmp[n-2][1]+1)
