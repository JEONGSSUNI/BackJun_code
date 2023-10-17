kak = []
for _ in range(3) :
    kak.append(int(input()))

result = ''
for i in kak :
    if sum(kak) == 180 :
        if kak.count(i) == 3 :
            result = 'Equilateral'
            break
        elif kak.count(i) == 2 :
            result = 'Isosceles'
            break
        else :
            result = 'Scalene'
    else :
        result = 'Error'

print(result)