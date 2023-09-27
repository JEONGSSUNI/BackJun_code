n, m = map(int, input().split())

n_list = [i+1 for i in range(n)]

for k in range(m) :
    i, j = map(int, input().split())
    temp = n_list[i-1:j]
    temp.reverse()
    n_list[i-1:j] = temp

for num in n_list :
    print(num, end=" ")

# 해당 구간의 리스트를 추출 후 값을 reverse() 후 다시 재할당
# for문으로 오름차순 정렬처럼 구현 시도했으나 1,2,3,4 → 2,3,4,1로 됨
# 리스트의 값을 reverse()할 생각을 못함 ∵ 리스트의 인덱스를 변경해야한다는 생각에서 벗어나지 못함