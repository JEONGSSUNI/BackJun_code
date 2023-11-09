import sys
n = int(input())

n_list = [0] * 10001

for i in range(n) :
    # # append는 메모리 재할당이 되므로 메모리 초과 뜸
    # n_list.append(sys.stdin.readline())
    
    # # 빈 리스트에 인덱스 할당해서 값을 주는 것은 Index Error
    # n_list[i] = int(sys.stdin.readline())

    # 10001개의 인덱스를 가지므로 sort는 비효율
    # 입력 받은 값을 인덱스로 지정하여 해당 인덱스 값을 1로 주기
    num = int(sys.stdin.readline())
    n_list[num] += 1 # 중복으로 입력받는 수가 있을 수 있으니까 + 1을 한다

# n_list.sort()

for i in range(10001) :
    if n_list[i] != 0 :
        for j in range(n_list[i]) :
            print(i)