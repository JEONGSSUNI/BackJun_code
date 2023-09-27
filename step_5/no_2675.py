n = int(input())
str_list = []
for i in range(n) :
    new_string = ''
    num, string = input().split()
    num = int(num)
    for s in string :
        new_string += s * num
    str_list.append(new_string)

for li in str_list :
    print(li)