x, y, w, h = map(int, input().split())

data = [x, w-x, y, h-y]
print(min(data))