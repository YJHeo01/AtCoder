ab,ac,bc = input().split()
a,b,c = 0,0,0
if ab == '<':b += 1
else: a += 1

if bc == '<':c += 1
else: b += 1

if ac == '<': c += 1
else: a += 1

if a == 1:
    print('A')

if b == 1:
    print('B')

if c == 1:
    print('C')
