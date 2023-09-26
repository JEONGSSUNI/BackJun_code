n, x = map(int, input().split())
n_list = list(map(int, input().split()))

for num in n_list :
    if x > num :
        print(num, end=' ')