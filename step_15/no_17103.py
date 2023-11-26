import sys
import math

n = int(sys.stdin.readline())
n_list = []
for _ in range(n) :
    n_list.append(int(sys.stdin.readline()))

max_n = max(n_list)

# 소수 리스트 생성
prime_list = [True] * (max_n + 1)

# 0과 1은 소수가 아님
prime_list[0], prime_list[1] = False, False

for i in range(2, int(math.sqrt(max_n)) + 1) :
    if prime_list[i] :
        for j in range(i+i, max_n + 1, i) :
            prime_list[j] = False

# 문제 풀이
for num in n_list :
    count = 0
    for i in range(2, (num // 2) + 1) :
        if prime_list[i] and prime_list[num-i] : # 순서가 바뀐 소수 세는 것 방지
            count += 1
    print(count)