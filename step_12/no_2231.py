n = int(input())

# for i in map(int, str(n)) :
#     print(i)

for num in range(1, n+1) :
    n_sum = sum(map(int, str(num)))
    constructor = num + n_sum
    if constructor == n :
        print(num)
        break
    if num == n :
        print(0)

# sum()함수를 사용하여 각 자리수의 합을 구함
# map(int, str(n)을 활용하여 각 자리수를 쉽게 가져올 수 있음
# num + 각 자리수의 값이 n과 같으면 그것이 가장 작은 생성자임을 알 수 있음
# 왜냐하면 1부터 n+1까지 순서대로 분해합을 구하므로 n과 같은 값이 나오는 순간이 가장 작은 생성자임
# range(1, n+1)인 이유 : for문이 n-1까지 돌게 되므로 n까지 돌게 n+1로 범위를 지정함