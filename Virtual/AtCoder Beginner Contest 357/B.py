#문자열 관련 함수를 이용하면 쉽게 해결할 수 있는 문제

def main():
    up_score = 0
    down_score = 0
    array = list(input())
    for i in array:
        if i.islower() == True:
            down_score += 1
        else:
            up_score += 1
    if up_score > down_score:
        for i in array:
            print(i.upper(),end="")
    else:
        for i in array:
            print(i.lower(),end="")
if __name__  == "__main__":
    main()
