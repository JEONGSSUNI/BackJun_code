n, m = map(int, input().split())
a = []
b = []
for i in range(n * 2) :
    if i >= n :
        b.append(list(map(int, input().split())))
    else :
        a.append(list(map(int, input().split())))
# a_b_plus = []
for i in range(n) :
    for j in range(m) :
        # a_b_plus.append(a[i][j] + b[i][j])
        print(a[i][j] + b[i][j], end=' ')
    print()

# for i in range(0, len(a_b_plus), m) :
#     for j in range(m) :
#         print(a_b_plus[i+j], end=' ')
#     print()