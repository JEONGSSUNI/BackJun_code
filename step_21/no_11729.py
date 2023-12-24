# def hanoi_tower(n, start, end)  :
#     if n == 1 :
#         print(start, end)
#         return
#
#     hanoi_tower(n-1, start, 6-start-end)
#     print(start, end)
#     hanoi_tower(n-1, 6-start-end, end)
#
# n = int(input())
# print(2 ** n-1)
# hanoi_tower(n, 1, 3)

# num : 원판의 개수
# from_ : 시작하는 장대 번호
# to_ : 옮기려는 장대 번호
# other : 나머지 하나 남은 장대 번호
def hanoi(num, from_, to_, other) : # 트리를 InOrder로 순회
    if num == 0 :
        return

    hanoi(num-1, from_, other, to_)
    print(from_, to_)
    hanoi(num-1, other, to_, from_)

n = int(input())
print((2 ** n) - 1) # 하노이탑 최소 이동 횟수 출력
hanoi(n, 1, 3, 2)