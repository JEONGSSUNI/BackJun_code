n_list = []
while True :
    n = int(input())
    if n == -1 :
        break
    else :
        n_list.append(n)

factor_list = []
for i in n_list :
    factor = ''
    hap = 0
    for j in range(1, i) :
        if i % j == 0 :
           factor += str(j) + " + "
           hap += j
        else :
            continue
    if i == hap :
        factor_list.append(factor[:-3])
    else :
        factor_list.append('is NOT perfect.')

for k in range(len(factor_list)) :
    if factor_list[k][0] == 'i' :
        print(str(n_list[k]), factor_list[k])
    else :
        print(str(n_list[k]), "=", factor_list[k])