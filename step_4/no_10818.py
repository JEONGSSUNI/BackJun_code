n = int(input())
n_list = [n]
n_list = list(map(int, input().split()))

n_min, n_max = n_list[0], n_list[0]
for num in n_list :
    if n_min > num :
        n_min = num
    if n_max < num :
        n_max = num

print(n_min, n_max)
print(min(n_list), max(n_list))
