import sys

n = int(sys.stdin.readline())
n_list = []

for _ in range(n) :
    n_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

minium = 110419
visited = [False for _ in range(n)]

def dfs(L, idx) :
    global minium
    if L == n // 2 :
        A = 0
        B = 0
        for i in range(n) :
            for j in range(n) :
                if visited[i] and visited[j] :
                    A += n_list[i][j]
                elif not visited[i] and not visited[j] :
                    B += n_list[i][j]

        minium = min(minium, abs(A-B))
        return

    for i in range(idx, n) :
        if not visited[i] :
            visited[i] = True
            dfs(L+1, i+1)
            visited[i] = False

dfs(0, 0)
print(minium)