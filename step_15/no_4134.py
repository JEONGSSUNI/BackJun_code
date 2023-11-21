import math
def prime(num) :
    # 소수찾기 알고리즘
    # 약수의 특성을 이용! 약수는 가운데의 수를 중심으로 약수가 대칭됨
    # 가운데 수 구하기 = 루트(num)까지 비교하면 됨
    if num == 0 or num == 1 :
        return False
    for i in range(2, int(math.sqrt(num)) + 1) : # 루트(num)까지 비교해야하므로 +1을 함
        if num % i == 0 :
            return False
    return True

n = int(input())

for _ in range(n) :
    x = int(input())
    while True :
        # if 숫자 == True일때 1이 아닌 숫자는 False로 처리
        # 0 == False, 1 == True / 나머지는 전부 인식 못함
        if prime(x) == True :
            print(x)
            break
        else :
            x += 1