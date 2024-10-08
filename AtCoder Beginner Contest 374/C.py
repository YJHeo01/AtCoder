def main():
    n = int(input())
    array = list(map(int,input().split()))
    length = 2 ** n
    answer = int(1e10)
    for i in range(length):
        a,b = 0,0
        for j in range(n):
            if i % 2 == 0:
                b += array[j]
            else:
                a += array[j]
            i = i // 2
        answer = min(answer,max(a,b))
    print(answer)

if __name__ == "__main__":
    main()
