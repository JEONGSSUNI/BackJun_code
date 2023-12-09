n = int(input())

# for문 사용
result = 1
if n == 0 :
    result = 1
else :
    for i in range(1, n+1) :
        result *= i

print(result)

# 함수 이용
import math
print(math.factorial(n))