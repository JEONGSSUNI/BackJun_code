n_set = set()
for i in range(10) :
    data = int(input())
    n_set.add(data % 42)

print(len(n_set))

# 중복없는 자료형 set
# set의 값 추가 = set.add(값)
