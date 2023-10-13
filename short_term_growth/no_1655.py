# # 시간초과
# n = int(input())
#
# num_list = []
# median_list = []
# for i in range(n) :
#     num_list.append(int(input()))
#     num_list.sort()
#     if len(num_list) % 2 == 0 :
#         median_list.append(num_list[(len(num_list)//2) - 1])
#     else :
#         median_list.append(num_list[len(num_list)//2])
#
# for data in median_list :
#     print(data)

# 우선순위 큐 사용
import heapq
import sys

n = int(sys.stdin.readline())

leftHeap = []
rightHeap = []
for i in range(n):
    num = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    print(-leftHeap[0])
