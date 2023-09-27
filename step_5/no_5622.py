call_string = input()
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
call_list = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]

sum = 0
for st in call_string :
    sum += call_list[abc.index(st)]

print(sum + len(call_string))

# # 더 간단함
# alpabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# call_string = input()
#
# time = 0
# for call in call_string :
#     for i in alpabet_list :
#         if call in str(i) :
#             time += alpabet_list.index(i) + 3
# print(time)