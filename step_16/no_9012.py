# 1. string에서 pop으로 한개씩 빼서 ()의 갯수를 각각 세서 같으면 yes, 다르면 no
# 문제점 : string에서는 pop을 할 수 없음
# 2. string.count해서 갯수가 같으면 yes, 다르면 no
# 문제점 : ())(()이면 갯수가 같으므로 yes가 나옴 답은 no인데...
# 3. [참고] stack에 (를 담고 )가 있으면 pop하기 / 만약에 pop이 안되면 그것은 no
# (가 먼저 나오는 것이므로!!! pop이 안되면 무조건 no

import sys
n = int(sys.stdin.readline())

for _ in range(n) :
    input_str = sys.stdin.readline().rstrip()
    stack = []
    for s in input_str :
        if s == '(' :
            stack.append(s)
        else :
            if stack :
                stack.pop()
            else :
                print('NO')
                break
    else :
        if not stack :
            print('YES')
        else :
            print('NO')