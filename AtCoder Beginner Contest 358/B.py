n,a = map(int,input().split())

array = list(map(int,input().split()))

cur_time = 0

for i in range(n):
    cur_time = max(cur_time+a,array[i]+a)
    print(cur_time)
