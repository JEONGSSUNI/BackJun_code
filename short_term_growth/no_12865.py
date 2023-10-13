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

dp = [[0]*(k+1) for _ in range(n + 1)] # n행, k열의 2차원 배열 생성
thing_list = [[0, 0]] # 왜 0번 인덱스에 [0, 0]을 넣어야하는가?

for i in range(n) :
    thing_list.append(list(map(int, input().split())))

for i in range(1, n+1) :
    w = thing_list[i][0]
    v = thing_list[i][1]

    for j in range(1, k+1) :
        if j < w :
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
print(dp[n][k])
