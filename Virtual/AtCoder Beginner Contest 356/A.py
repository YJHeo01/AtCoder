n,l,r = map(int,input().split())
a = list(range(n+1))
left, right = l,r
while True:
    if right <= left:
        break
    a[left], a[right] = a[right], a[left]
    left += 1; right -= 1
print(*a[1:])
