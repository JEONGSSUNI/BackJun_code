x = int(input())
y = int(input())

if -1000 <= x <= 1000 and -1000 <= y <= 1000 and x != 0 and y != 0 :
    if x > 0 :
        if y > 0 :
            print(1)
        else :
            print(4)
    else :
        if y > 0 :
            print(2)
        else :
            print(3)
else :
    print('-1000이상 1000이하인 0이 아닌 정수를 입력하세요.')