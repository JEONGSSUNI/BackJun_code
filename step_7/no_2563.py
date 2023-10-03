# 색종이 수 n
# i j : 왼쪽 아래 꼭지점의 위치 i는 x축, j는 y축임
# 넓이 : n * 100 / 색종이 가로 세로 각각 10
# 전체 넓이 : n * 100 - 겹치는 영역
# 예시 300 - 5 * 8 = 300 - 40 = 260

# 2차원 배열로 전체 크기를 할당 후 1의 개수를 구함
area = [[0 for i in range(100)] for i in range(100)] # 100 X 100 크기 도화지
n = int(input())
for num in range(n) :
    i, j = map(int, input().split())
    for x in range(i, i+10) :
        for y in range(j, j+10) :
            area[x][y] = 1

total_area = 0
for one_list in area :
    total_area += one_list.count(1)

print(total_area)