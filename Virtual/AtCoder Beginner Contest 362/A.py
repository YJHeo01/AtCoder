r,g,b = map(int,input().split())
c = input()

if c == "Blue":
    print(min(r,g))
elif c == "Red":
    print(min(g,b))
else:
    print(min(r,b))
