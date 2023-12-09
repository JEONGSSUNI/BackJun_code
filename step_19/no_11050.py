n, k = map(int, input().split())

# for문
result = 1
for i in range(k+1, n+1) :
    result *= i

for i in range(1, (n-k)+1) :
    result //= i

print(result)

# 함수 이용
import math
print(math.comb(n, k))