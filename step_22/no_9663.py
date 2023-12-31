# def n_queens(n) :
#     def backtracking(row, diagonals, anti_diagonals, cols) :
#         if row == n :
#             return 1
#
#         solutions = 0
#
#         for col in range(n) :
#             curr_diagonal = row - col
#             curr_anti_diagonal = row + col
#
#             if (col in cols
#                     or curr_diagonal in diagonals
#                     or curr_anti_diagonal in anti_diagonals) :
#                 continue
#
#             cols.add(col)
#             diagonals.add(curr_diagonal)
#             anti_diagonals.add(curr_anti_diagonal)
#
#             solutions += backtracking(row+1, diagonals, anti_diagonals, cols)
#
#             cols.remove(col)
#             diagonals.remove(curr_diagonal)
#             anti_diagonals.remove(curr_anti_diagonal)
#
#         return solutions
#
#     return backtracking(0, set(), set(), set())
#
# n = int(input())
# print(n_queens(n))


## -------------------------------------------------- ##
n = int(input())
ans = 0
row = [0] * n

def is_promising(x) :
    for i in range(x) :
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i) :
            return False
    return True


def n_queens(x) :
    global ans
    if x == n :
        ans += 1
        return
    else :
        for i in range(n) :
            row[x] = i
            if is_promising(x) :
                n_queens(x+1)

n_queens(0)
print(ans)