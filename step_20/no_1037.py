n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
# n_list는 진짜 약수이므로 정렬해서 맨 첫번째 원소와 마지막 원소를 곱하면 n임
print(n_list[0] * n_list[-1])