# 각 x, y값이 두번씩 입력되므로 x, y좌표가 list에 있으면 remove, 없으면 append해서 최종 1개만 남음
x_data = []
y_data = []
for _ in range(3) :
    x, y = map(int, input().split())

    if x in x_data :
        x_data.remove(x)
    else :
        x_data.append(x)

    if y in y_data :
        y_data.remove(y)
    else :
        y_data.append(y)

print(x_data[0], y_data[0])

# 다른 사람 답안
x_data = []
y_data = []

for _ in range(3) :
    x, y = map(int, input().split())
    x_data.append(x)
    y_data.append(y)

for i in range(3) :
    if x_data.count((x_data[i])) == 1 :
        answer_x = x_data[i]
    if y_data.count((y_data[i])) == 1:
        answer_y = y_data[i]
print(answer_x, answer_y)