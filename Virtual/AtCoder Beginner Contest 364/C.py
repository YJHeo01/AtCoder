n,x,y = map(int,input().split())

sweet = sorted(list(map(int,input().split())))
salt = sorted(list(map(int,input().split())))

sweet_cnt = 0
salt_cnt = 0

while sweet:
    sweet_cnt += 1
    tmp = sweet.pop()
    x -= tmp
    if x < 0: break

while salt:
    salt_cnt += 1
    tmp = salt.pop()
    y -= tmp
    if y < 0: break

print(min(sweet_cnt,salt_cnt))
