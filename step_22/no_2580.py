import sys

graph = []
blank = []

for i in range(9) :
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9) :
    for j in range(9) :
        if graph[i][j] == 0 :
            blank.append((i, j))

def checkRow(x, a) :
    for i in range(9) :
        if a == graph[x][i] :
            return False
    return True

def checkCol(y, a) :
    for i in range(9) :
        if a == graph[i][y] :
            return False
    return True

def checkRect(x, y, a) :
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3) :
        for j in range(3) :
            if a == graph[nx + i][ny + j] :
                return False
    return True

def dfs(idx) :
    if idx == len(blank) :
        for i in range(9) :
            print(*graph[i])
        exit(0)

    for i in range(1, 10) :
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i) :
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0

dfs(0)


############################
def row(a, n): # 가로
    for i in range(9):
        if n == sudoku[a][i]: # 이미 있으면
            return False
    return True

def column(a, n): # 세로
    for i in range(9):
        if n == sudoku[i][a]: # 이미 있으면
            return False
    return True

def square(y, x, n): # 3x3 칸
    for i in range(3):
        for j in range(3):
            if n == sudoku[y//3 * 3 + i][x//3 * 3 + j]: # 칸내에 이미 있으면
                return False
    return True

def find(n):
    if n == len(blank): # 빈 공간 만큼 사용했으면
        for i in sudoku: # 출력 후
            print(*i)
        exit() # 강제 종료

    for i in range(1,10):
        y = blank[n][0]
        x = blank[n][1]
        if column(x,i) and row(y,i) and square(y, x, i):
            sudoku[y][x] = i
            find(n+1)
            sudoku[y][x] = 0

import sys
sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i,j])
find(0)