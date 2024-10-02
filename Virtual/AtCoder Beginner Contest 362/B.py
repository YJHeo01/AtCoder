xa,ya = map(int,input().split())
xb,yb = map(int,input().split())
xc,yc = map(int,input().split())

line = [(xa-xb)**2+(ya-yb)**2,(xb-xc)**2+(yb-yc)**2,(xa-xc)**2+(ya-yc)**2]
line.sort()

if line[0] + line[1] == line[2]:
    print("Yes")
else:
    print("No")
