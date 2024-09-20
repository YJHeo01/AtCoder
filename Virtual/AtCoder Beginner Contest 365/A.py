y = int(input())

if y % 4 != 0:
    print(365)
else:
    if y % 100 != 0:
        print(366)
    elif y % 100 == 0 and y % 400 != 0:
        print(365)
    else:
        print(366)
