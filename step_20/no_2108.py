import sys
n = int(sys.stdin.readline())

n_list = []
for _ in range(n) :
    n_list.append(int(sys.stdin.readline()))

n_list.sort()

# 산술평균
print(round(sum(n_list)/n))

# 중앙값
print(n_list[n//2])

# 최빈값
mode = dict()
for num in n_list :
    if num in mode :
        mode[num] += 1
    else :
        mode[num] = 1

maximum = max(mode.values())
max_dic = []

for i in mode :
    if maximum == mode[i] :
        max_dic.append(i)

if len(max_dic) > 1 :
    print(max_dic[1])
else :
    print(max_dic[0])

# 범위
print(n_list[-1] - n_list[0])