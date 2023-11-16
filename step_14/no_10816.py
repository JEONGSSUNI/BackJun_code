import sys
n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))

n_dict = {}
for num in n_list :
    if num in n_dict :
        n_dict[num] += 1
    else :
        n_dict[num] = 1

m = int(input())
m_list = list(map(int, sys.stdin.readline().split()))

# # dictionary 이용
# for num in m_list :
#     try :
#         n_dict[num]
#     except KeyError :
#         print(0, end=' ')
#     else :
#         print(n_dict[num], end=' ')

# 이분 탐색
def binarySearch(arr, target, start, end) :
    if start > end :
        return 0
    mid = (start + end) // 2
    if arr[mid] == target :
        return n_dict.get(target)
    elif arr[mid] < target :
        return binarySearch(arr, target, mid + 1, end)
    else :
        return binarySearch(arr, target, start, mid - 1)

for target in m_list :
    print(binarySearch(n_list, target, 0, len(n_list)-1), end=' ')