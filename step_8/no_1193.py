# 한줄 실행 할 때마다 원소의 갯수가 1개씩 증가함
# [1/1], [1/2, 2/1], [3/0, 2/1, 1/3], ...
# 짝수번 째 줄은 분모가 내림차순, 분자가 오름차순이고 홀수번 째 줄은 그 반대
n = int(input())
line = 1
while n > line :
    n -= line
    line += 1

if line % 2 == 0 :
    up = n
    down = line - n + 1
else :
    up = line - n + 1
    down = n
print(up, '/', down, sep='')

# # 직접 코드 짰지만 시간 초과
# n = int(input()) - 1
# i = 0
# j = 0
# while n != 0 :
#     if i == 0 :
#         j += 1
#         n -= 1
#         if n == 0 : break
#         while j > 0 :
#             i += 1
#             j -= 1
#             n -= 1
#             if n == 0: break
#     else :
#         if j == 0 :
#             i += 1
#             n -= 1
#             if n == 0: break
#             while i != 0 :
#                 i -= 1
#                 j += 1
#                 n -= 1
#                 if n == 0: break
# print(str(i+1) + '/' + str(j+1))