a,b,c,d,e,f = map(int,input().split())
g,h,i,j,k,l = map(int,input().split())
answer = "Yes"

if g >= d or j <= a:
    answer = 'No'

if h >= e or k <= b:
    answer = "No"

if i >= f or l <= c:
    answer = "No"

print(answer)
