n = int(input())

n_list = []
for _ in range(n) :
    n_list.append(int(input()))

n_list = sorted(n_list)

# 버블 정렬
for i in range(0, n) :
    for j in range(0, n) :
        if n_list[i] < n_list[j] :
            n_list[i], n_list[j] = n_list[j], n_list[i]

# 삽입 정렬
for i in range(1, n) :
    while (i > 0) & (n_list[i] < n_list[i-1]) :
        n_list[i], n_list[i-1] = n_list[i-1], n_list[i]
        i -= 1

for i in range(n) :
    print(n_list[i])