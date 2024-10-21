n = int(input())
A = sorted(list(map(int,input().split())),reverse=True)
B = sorted(list(map(int,input().split())),reverse=True)

tmp = False
x = A[0]

A_idx, B_idx = 0,0

while True:
    if B_idx == n-1:
        if A_idx == B_idx:
            x = A[n-1]
        break
    if A_idx == n:
        break
    if A[A_idx] <= B[B_idx]:
        A_idx += 1
        B_idx += 1
    else:
        if tmp == True:
            x = -1
            break
        tmp = True
        x = A[A_idx]
        A_idx += 1

print(x)
