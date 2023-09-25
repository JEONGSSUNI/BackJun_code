A, B = map(int, input().split())

if -10000 <= A <= 10000 :
    if -10000 <= B <= 10000 :
        if A < B :
            print("<")
        elif A > B :
            print(">")
        else :
            print("==")
else :
    print("-10000이상 10000이하 숫자를 입력하세요.")