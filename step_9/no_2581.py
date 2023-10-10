m = int(input())
n = int(input())

factor_list = []
for num in range(m, n+1) :
    if num > 1 :
        count = 2
        error = 0
        while num > count :
            if num % count == 0 :
                error += 1
                break
            count += 1
        if error == 0 :
            factor_list.append(num)

if len(factor_list) == 0 :
    print(-1)
else :
    print(sum(factor_list))
    print(factor_list[0])