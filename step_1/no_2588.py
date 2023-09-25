A = int(input())
B = int(input())

if 100 <= A <= 999 :
    if 100 <= B <= 999:
        B_100 = B // 100
        B_10 = (B // 10) - (B_100 * 10)
        B_1 = B % 10
        print(A * B_1)
        print(A * B_10)
        print(A * B_100)
        print(A * B)
else :
    print('3자리 양수를 입력하세요.')