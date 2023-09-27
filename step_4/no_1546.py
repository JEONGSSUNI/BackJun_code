n = int(input())
score_list = [0 for i in range(n)]
score_list = list(map(int, input().split()))

max_score = max(score_list)
sum = 0

for idx in range(len(score_list)) :
    score_list[idx] = score_list[idx] / max_score * 100
    sum += score_list[idx]

print(sum / len(score_list))
# print(sum(score_list) / len(score_list))
# import statistics
# print(statistics.mean(score_list))

# 리스트 평균을 구하는 함수가 없음
# for문을 이용한 평균 계산하기 → 내가 코딩한 방법
# 내장함수 sum, len을 활용한 평균 계산하기
# statistics로 평균 계산하기