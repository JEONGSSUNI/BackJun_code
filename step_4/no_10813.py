n, m = map(int, input().split())
n_list = [i + 1 for i in range(n)]

for j in range(m) :
    i, j = map(int, input().split())
    temp = n_list[i-1]
    n_list[i-1] = n_list[j-1]
    n_list[j-1] = temp

for num in n_list :
    print(num, end=" ")
