import math

# 에라토스테네스의 체
# 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법
# 1 제거 → 2를 소수로 채택 후 2의 배수 제거 → 3을 소수로 채택 후 3의 배수 제거 → 제일 작은 소수 채택 후 소수의 배수 제거 반복
def eratostenes(low, upper):
    prime_list = [True] * (upper + 1)
    
    # 에라토스테네스의 체
    prime = int(math.sqrt(upper))
    for i in range(2, prime+1) :
        if prime_list[i] == True :
            for j in range(i+i, upper+1, i) :
                prime_list[j] = False
                
    # low이상의 숫자 중 소수를 구하는 것이므로 low이하의 숫자는 False
    for i in range(low) :
        prime_list[i] = False

    # 0과 1은 소수가 아님
    result_list = [i for i in range(2, upper+1) if prime_list[i] == True]
    return result_list

m, n = map(int, input().split())
result = eratostenes(m, n)
for num in result :
    print(num)