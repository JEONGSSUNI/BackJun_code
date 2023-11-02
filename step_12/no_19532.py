# # ZeroDivision Error
# n_list = list(map(int, input().split()))
# y = ((n_list[2] * n_list[3]) - (n_list[5] * n_list[0])) // ((n_list[1] * n_list[3]) - (n_list[4] * n_list[0]))
# x = (n_list[2] - (n_list[1] * y)) // n_list[0]
# print(x, y)

# 간단하게
a, b, c, d, e, f = map(int, input().split())
x = ((c * e) - (f * b)) // ((a * e) - (b * d))
y = ((c * d) - (f * a)) // ((b * d) - (a * e))
print(x, y)

# 모든 경우의 수 (브루트 포스)
a, b, c, d, e, f = map(int, input().split())
for i in range(-999, 1000) :
    for j in range(-999, 1000) :
        if (a * i) + (b * j) == c and (d * i) + (e * j) == f :
            print(i, j)