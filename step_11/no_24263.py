# 시간 복잡도 알고리즘

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         sum <- sum + A[i]; # 코드1
#     return sum;
# }

# 입력받은 n을 넣으면 1부터 n까지의 인덱스에 해당하는 값을 sum을 더한다
# sum 값을 출력

# 즉, 시간 복잡도는 O(n)
# n번 수행
# n이 어떤 값이어도 최고차항은 1

n = int(input())
print(n) # 수행 횟수
print(1) # 최고차항