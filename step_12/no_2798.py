n, m = map(int, input().split())
n_list = list(map(int, input().split()))

sum_list = set()

for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            hap = n_list[i] + n_list[j] + n_list[k]
            if hap <= m :
                sum_list.add(hap)
            else :
                continue
print(max(sum_list))