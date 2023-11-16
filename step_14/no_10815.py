import sys
# 시간초과
n = int(input())
have_list = list(map(int, sys.stdin.readline().split()))

m = int(input())
m_list = list(map(int, sys.stdin.readline().split()))

# correct = []
#
# for num in m_list :
#     if num in have_list :
#         correct.append(1)
#     else :
#         correct.append(0)
#
# for num in correct :
#     print(num, end=' ')

# dictionary가 빠름 ∵ 일일히 확인하는 과정을 축소시킴
correct_dic = {}
for i in m_list :
    correct_dic[i] = 0

for num in have_list :
    if num in correct_dic :
        correct_dic[num] = 1

for i in correct_dic :
    print(correct_dic[i], end=' ')