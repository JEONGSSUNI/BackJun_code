t = int(input())

# for문 이용
for _ in range(t) :
    n, m = map(int, input().split())

    result = 1
    for i in range(n+1, m+1) :
        result *= i
    for i in range(1, (m-n)+1) :
        result //= i

    print(result)

# 함수 이용
import math
print(math.comb(m, n))