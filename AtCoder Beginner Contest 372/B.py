answer = []
value = int(input())
for i in range(10,-1,-1):
    while True:
        if 3 ** i > value:
            break
        answer.append(i)
        value -= 3 ** i
print(len(answer))
for i in answer:
    print(i,end=" ")
