y = int(input())

if 1 <= y <= 4000 :
    if y % 4 == 0 :
        if y % 100 != 0 or y % 400 == 0:
            print(1)
        else :
            print(0)
    else :
        print(0)
else :
    print('1년 이상 4000년 이하로 입력하세요.')