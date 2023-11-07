# import numpy as np

n_list = []
n_sum = 0

for _ in range(5) :
    num = int(input())
    n_list.append(num)
    n_sum += num

n_list = sorted(n_list)

print(n_sum // 5)
print(n_list[2])

# print(int(np.mean(n_list)))
# print(int(np.median(n_list)))

