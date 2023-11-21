import math
import sys

# 시간초과
def prime_count(num) :
    if num == 1 :
        return False
    else :
        for i in range(2, int(math.sqrt(num)+1)) :
            if num % i == 0 :
                return False
        return True

while True :
    n = int(sys.stdin.readline())

    if n == 0 :
        break

    count = 0
    for i in range(n, 2*n+1) :
        if prime_count(i) :
            count += 1
    print(count)

# 시간초과 해결 : 미리 최댓값까지의 소수를 판별 후 해당 범위내에서 소수 개수 count
m = 123456 # 문제에서 주어진 최댓값
prime_list = [True] * ((2 * m) + 1)

# 0과 1은 소수가 아님
prime_list[0], prime_list[1] = False, False

for i in range(2, int(math.sqrt(2 * m)) + 1) :
    if prime_list[i] :
        for j in range(i+i, (2 * m) + 1, i) :
            prime_list[j] = False

while True :
    n = int(sys.stdin.readline())

    if n == 0 :
        break

    count = 0
    for i in range(n+1, 2*n+1) :
        if prime_list[i] == True :
            count += 1
    print(count)