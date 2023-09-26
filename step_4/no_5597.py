work_list = [i+1 for i in range(30)]
for i in range(28) :
    data = int(input())
    work_list.remove(data)
print(min(work_list))
print(max(work_list))

# 답안 참고함
# list.remove 함수를 생각 못 함
