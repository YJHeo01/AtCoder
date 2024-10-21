n,q = map(int,input().split())
left, right = 1,2
answer = 0
for _ in range(q):
    h,t = input().split()
    t = int(t)
    if h == 'L':
        if t > left:
            if right > t or right < left:
                answer += (t-left)
            else:
                answer += (n-t+left)
        else:
            if right < t or right > left:
                answer += (left-t)
            else:
                answer += (n-left+t)
        left = t
    else:
        if t > right:
            if left > t or left < right:
                answer += (t-right)
            else:
                answer += (n-t+right)
        else:
            if left < t or left > right:
                answer += (right-t)
            else:
                answer += (n-right+t)
        right = t
print(answer)
