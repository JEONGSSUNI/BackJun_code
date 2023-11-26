import math

n = int(input())

window = [0] * (n+1)

# 메모리 초과
for i in range(1, n+1) :
    count = 1
    while (count * i) <= n :
        if window[count * i] == 1 :
            window[count * i] = 0
        else :
            window[count * i] = 1
        count += 1

print(window.count(1))

# 다른 풀이
# 1을 결과로 갖는 창문들은 어떤 수의 제곱수 ex) 1, 4, 9, ...
# n 이하의 제곱수의 개수는 루트 n개
print(int(math.sqrt(n)))