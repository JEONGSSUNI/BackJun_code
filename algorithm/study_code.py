# ---------------------------------------------------- #
# 절댓값 구하기
import math
# 1
def abs_sign(a) :
    if a >= 0 :
        return a
    else :
        return -a

# 2
def abs_square(a) :
    b = a * a
    return math.sqrt(b) # sqrt는 결과를 소수점이 붙은 값으로 돌려줌

# print(abs_sign(-3))
# print(abs_sign(5))
# print()
# print(abs_square(-3))
# print(abs_square(5))

# ---------------------------------------------------- #
# 1부터 n까지의 합 구하기
def sum_n_while(n) :
    i = 1
    final_sum = 0
    while n >= i :
        final_sum += i
        i += 1
    return final_sum

def sum_n_for(n) :
    s = 0
    for i in range(1, n+1) :
        s += i
    return s

def sum_n_gauss(n) :
    return n * (n + 1) // 2 # 1 + 100 = 101, 2 + 99 = 101 ...이 n/2개 존재

# print(sum_n_while(10))
# print(sum_n_for(100))
# print(sum_n_gauss(100))

# ---------------------------------------------------- #
# 동명이인 찾기 / O(n^2) = O(1/2(n^2) - 1/2(n))
def find_same_name(name_list) :
    n = len(name_list)
    result = set()

    for i in range(0, n-1) :
        for j in range(i+1, n) :
            if name_list[i] == name_list[j] :
                result.add(name_list[i])
    return result

name = ['Tom', 'Jerry', 'Mike', 'Tom']
# print(find_same_name(name))

name = ['Tom', 'Jerry', 'Mike', 'Tom', 'Mike']
# print(find_same_name(name))

# ---------------------------------------------------- #
#