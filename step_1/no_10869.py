A, B= map(int, input().split())

if 1 <= A <= 10000 :
    if 1 <= B <= 10000 :
        print(A + B)
        print(A - B)
        print(A * B)
        print(A // B)
        print(A % B)
else :
    print('10,000이하의 양수를 입력해주세요.')