n,k = map(int,input().split())
array = list(map(int,input().split()))

for i in range(n-k,n):
    print(array[i],end=" ")

for i in range(n-k):
    print(array[i],end=" ")
