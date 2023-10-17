n = int(input())

x_data = []
y_data = []
for _ in range(n) :
    x, y = map(int, input().split())
    x_data.append(x)
    y_data.append(y)


hor = max(x_data) - min(x_data)
ver = max(y_data) - min(y_data)
print(hor * ver)