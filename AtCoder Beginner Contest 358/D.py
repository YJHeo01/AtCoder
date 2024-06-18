def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(); b.sort()
    answer = 0
    a_idx = 0
    for i in range(m):
        while True:
            if a_idx == n:
                answer = -1
                break
            if a[a_idx] >= b[i]:
                answer += a[a_idx]
                break
            a_idx += 1
        if answer == -1:break
        a_idx += 1
    print(answer)

if __name__  == "__main__":
    main()
