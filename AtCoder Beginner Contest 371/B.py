n,m = map(int,input().split())

not_first_son = [False] * (n+1)

for _ in range(m):
    a,b = input().split()
    i = int(a)
    if b == 'M' and not_first_son[i] == False:
        not_first_son[i] = True
        print("Yes")
    else:
        print("No")
