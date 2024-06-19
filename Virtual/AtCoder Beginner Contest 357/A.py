#https://atcoder.jp/contests/abc357/submissions/54703772
#간단한 시뮬레이션 문제

def main():
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    answer = n
    for i in range(n):
        m -= array[i]
        if m < 0:
            answer = i
            break
    print(answer)

if __name__  == "__main__":
    main()
