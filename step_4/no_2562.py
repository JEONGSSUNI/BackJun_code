n_list = []
for i in range(9) :
    n_list.append(int(input()))

for num in range(len(n_list)) :
    if n_list[num] == max(n_list) :
        print(n_list[num])
        print(num + 1)