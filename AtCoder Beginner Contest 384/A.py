n,c1,c2 = input().split()

s = list(input())

for c in s:
    if c != c1:
        print(c2,end="")
    else:
        print(c,end="")
