import sys

input = sys.stdin.readline

INF = int(1e9) + 1
n = int(input()) + 2
x = [-INF] + list(map(int,input().split())) + [INF]
p = [0] + list(map(int,input().split())) + [0]
prefix_sum = [0] * (n+1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + p[i]

q = int(input())

def get_left(point):
    ret_value = n
    left, right = 0,n-1
    while left <= right:
        mid = (left+right) // 2
        if x[mid] >= point:
            right = mid - 1
        else:
            left = mid + 1
            ret_value = mid
    return ret_value + 1

def get_right(point):
    ret_value = 0
    left, right = 0,n-1
    while left <= right:
        mid = (left+right) // 2
        if x[mid] > point:
            ret_value = mid
            right = mid - 1
        else:
            left = mid + 1
    return ret_value
 
for _ in range(q):
    l,r = map(int,input().split())
    if r < x[0] or l > x[n-1]:
        print(0)
        continue
    left = get_left(l)
    right = get_right(r)
    #print(left,right)
    print(prefix_sum[right]-prefix_sum[left])
