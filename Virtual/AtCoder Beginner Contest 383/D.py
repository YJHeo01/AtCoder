import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    prime_list = []
    n_root = int(math.sqrt(n))
    prime = [True] * (n_root+2)
    prime_cnt = 0
    for i in range(2,n_root+2):
        if prime[i]:
            prime_list.append(i)
            prime_cnt += 1
            for j in range(i,n_root+2,i):
                prime[j] = False
    answer = 0
    for start in range(prime_cnt):
        end = start
        left, right = start, prime_cnt - 1
        while left <= right:
            mid = (left+right) // 2
            if (prime_list[start] * prime_list[mid]) ** 2 <= n:
                end = mid
                left = mid + 1
            else:
                right = mid - 1
        answer += (end-start)
    for i in range(prime_cnt):
        if prime_list[i] ** 8 <= n:
            answer += 1
        else:
            break
    print(answer)

if __name__ == "__main__":
    main()
