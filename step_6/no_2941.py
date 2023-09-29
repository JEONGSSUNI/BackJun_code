input_str = input()
cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for cro in cro_list :
    input_str = input_str.replace(cro, '*')

print(len(input_str))

# replace()를 생각하지 못함
# in함수를 사용하려고 했으나 전부 2글자가 아니어서 실패