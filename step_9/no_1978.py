n = int(input())
n_list = list(map(int, input().split()))

primary = 0
for num in n_list :
    count = 1
    factor = 0
    while num >= count :
        if num % count == 0 :
            factor += 1
        count += 1
    if factor == 2 :
        primary += 1

print(primary)