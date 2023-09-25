A, B, C = map(int, input().split())

if 1 <= A <= 10**12 :
    if 1 <= B <= 10**12:
        if 1 <= C <= 10**12:
            print(A + B + C)
else :
    print("1이상 10^12이하 숫자를 입력하세요.")