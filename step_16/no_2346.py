from collections import deque
n = int(input())

# enumerate : (인덱스, 값) 구조로 저장
que = deque(enumerate(map(int, input().split())))

# deque의 rotate() 메서드
# deque를 num만큼 회전(양수면 오른쪽, 음수면 왼쪽)

ans = []

while que :
    idx, num = que.popleft()
    ans.append(idx + 1)

    if num > 0 :
        que.rotate(-(num -1))
    elif num < 0 :
        que.rotate(-num)

print(' '.join(map(str, ans)))