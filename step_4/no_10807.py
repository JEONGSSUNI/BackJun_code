n = int(input())
n_list = list(map(int, input().split()))
num = int(input())

# sum = 0
# for nn in n_list :
#     if nn == num :
#         sum += 1
# print(sum)

print(n_list.count(num))