# # 틀림
# n, k = map(int, input().split())
#
# thing_list = []
# for i in range(n) :
#     thing_list.append(list(map(int, input().split())))
#
# max_w = 0
# for i in range(0, n) :
#     j = 0
#     while j < n :
#         if i == j or i < j :
#             j += 1
#             break
#         if thing_list[i][0] + thing_list[j][0] <= k :
#             if max_w < thing_list[i][1] + thing_list[j][1] :
#                 max_w = thing_list[i][1] + thing_list[j][1]
#         j += 1
#
# print(max_w)

# 동적 프로그래밍 (DP)
n, k = map(int, input().split())

# dp = [[0 for _ in range(n + 1)][0 for _ in range(k + 1)]]


thing_list = []
for i in range(n) :
    thing_list.append(list(map(int, input().split())))
