hang_list = []
max_int = 0
hang = 0
for i in range(9) :
    hang_list.append(list(map(int, input().split())))
    if max_int < max(hang_list[i]) :
        max_int = max(hang_list[i])
        hang = i

for i in range(len(hang_list[hang])) :
    if max_int == hang_list[hang][i] :
        print(max_int)
        print(hang + 1, i + 1)