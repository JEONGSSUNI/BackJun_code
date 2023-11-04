# 브루트 포스 알고리즘 : 완전 탐색 알고리즘 (가능한 모든 수를 조합함)
# 생각을 조금 더 해볼 필요가 있음
# 막상 코드 구현해보면 쉬움

n = int(input())

count = 0
title = 666

while True :
    # 666이 들어간 숫자이면 시리즈로 작품이 나옴
    if '666' in str(title) : # title에 666이 있으면 count를 1 늘림
        count += 1
    
    # count와 n이 같다면 그떄의 title이 답임
    if count == n :
        break

    title += 1

print(title)