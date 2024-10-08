def main():
    s = list(input())
    t = list(input())
    answer = 0
    for i in range(min(len(s),len(t))):
        if s[i] != t[i]:
            answer = i + 1
            break
    if answer == 0 and (len(s) != len(t)):
        answer = min(len(s),len(t)) + 1
    print(answer)

if __name__ == "__main__":
    main()
