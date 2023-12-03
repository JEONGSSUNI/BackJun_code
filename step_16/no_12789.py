n = int(input())
n_list = list(map(int, input().split()))
stack = []
order = 1

while n_list :
    if order == n_list[0] :
        order += 1
        n_list.pop(0)
    else :
        stack.append(n_list.pop(0))

    while stack and stack[-1] == order :
        stack.pop()
        order += 1

if len(stack) == 0 :
    print("Nice")
else :
    print('Sad')