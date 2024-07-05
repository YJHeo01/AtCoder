#https://atcoder.jp/contests/abc360/submissions/55217228

def main():
    n = int(input())
    cnt = [0] * (n+1)
    max_value = [0] * (n+1)
    sum_value = [0] * (n+1)
    idx = list(map(int,input().split()))
    weight = list(map(int,input().split()))
    for i in range(n):
        cnt[idx[i]] += 1
        sum_value[idx[i]] += weight[i]
        max_value[idx[i]] = max(max_value[idx[i]],weight[i])
    answer = 0
    for i in range(1,n+1):
        answer += (sum_value[i]-max_value[i])
    print(answer)

if __name__ == "__main__":
    main()
