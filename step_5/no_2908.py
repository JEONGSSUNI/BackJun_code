num_list = list(map(int, input().split()))

for i in range(len(num_list)) :
    one = num_list[i] % 10
    ten = (num_list[i] // 10) % 10
    hun = num_list[i] // 100
    num_list[i] = (one * 100) + (ten * 10) + hun

print(max(num_list))

# # reverse()로 구하기
# a, b = input().split()
# # 문자열[시작:끝:step]
# a = int(a[::-1])
# b = int(b[::-1])
#
# if a > b :
#     print(a)
# else :
#     print(b)