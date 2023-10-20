# 시간 복잡도 알고리즘

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

# for문 i가 n번 반복, for문 j가 n번 반복
# sum의 결과를 출력

# O(n^2)의 시간 복잡도를 가짐
# 최고차항은 2로 고정

n = int(input())
print(n * n)
print(2)