# 시간 복잡도 알고리즘

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             for k <- 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

# i가 1~n번 수행
# i 한번에 j는 n번 수행
# j 한번에 k는 n번 수행
# O(n^3)이 시간 복잡도

n = int(input())
print(n**3)
print(3)