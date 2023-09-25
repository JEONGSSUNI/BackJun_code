A, B, C = map(int, input().split())

if 2 <= A <= 10000 :
    if 2 <= B <= 10000 :
        if 2 <= C <= 10000:
            print((A + B) % C)
            print(((A % C) + (B % C)) % C)
            print((A * B) % C)
            print(((A % C) * (B % C)) % C)
else :
    print('2이상 10,000이하의 양수를 입력해주세요.')