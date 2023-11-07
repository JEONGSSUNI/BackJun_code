n, k = map(int, input().split())

n_list = list(map(int, input().split()))
n_list.sort(reverse=True) # n_list = n_list.sort(reverse=True) 하면 안됨

print(n_list[k-1])

