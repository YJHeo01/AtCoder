n = int(input())
answer = 0
L_position, R_position = -1,-1
for _ in range(n):
    a,s = input().split()
    a = int(a)
    if s == 'L':
        if L_position != -1: answer += abs(a-L_position)
        L_position = a
    else:
        if R_position != -1: answer += abs(a-R_position)
        R_position = a
print(answer)
