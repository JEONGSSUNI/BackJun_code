# 재이해 필요
n, m = map(int, input().split())

matrix = []
count = []

for _ in range(n) :
    matrix.append(input())

for a in range(n-7) : # 8*8로 자르기 위해, -7해준다
    for b in range(m-7) :
        w_index = 0 # W로 시작할 때 경우의 수
        b_index = 0 # B로 시작할 때 경우의 수

        for i in range(a, a+8) : # 시작지점
            for j in range(b, b+8) :
                if (i + j) % 2 == 0 : # 짝수인 경우
                    if matrix[i][j] != 'W': # W가 아니면, 즉 B이면
                        w_index += 1 # W로 칠하는 갯수
                    else :
                        b_index += 1 # B로 칠하는 갯수
                else : # 홀수인 경우
                    if matrix[i][j] != 'W' :
                        b_index += 1
                    else :
                        w_index += 1

        count.append(w_index) # W로 시작할 때 경우의 수
        count.append(b_index) # B로 시작할 때 경우의 수
print(min(count))