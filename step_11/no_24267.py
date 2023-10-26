# 시간 복잡도 알고리즘

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

# i는 1~n-2번
# i 1번에 j는 i+1~n-1번
# j 1번에 k는 j+1~n번
# O(n^3) 시간복잡도를 가짐

n = int(input())
print(n*(n-1)*(n-2)//6)
print(3)