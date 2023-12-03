# import sys
# while True :
#     input_str = sys.stdin.readline()
#
#     if input_str == '.' :
#         break
#
#     stack = []
#
#     for s in input_str :
#         if s == '(' or s == '[' :
#             stack.append(s)
#         elif s == ')' :
#             if len(stack) != 0 or stack[-1] == '(' :
#                 stack.pop()
#             else :
#                 stack.append(s)
#                 break
#         elif s == ']' :
#             if len(stack) != 0 or stack[-1] == ']' :
#                 stack.pop()
#             else :
#                 stack.append(s)
#                 break
#     if len(stack) == 0 :
#         print('yes')
#     else :
#         print('no')

import sys

while True:
    str_val = sys.stdin.readline()
    if str_val == '.':
        break

    stack = []
    result = True

    for el in str_val:
        if el == '(' or el == '[':
            stack.append(el)
        elif el == ')':
            if len(stack) == 0 or stack[-1] == '[':
                result = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif el == ']':
            if len(stack) == 0 or stack[-1] == '(':
                result = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if len(stack) == 0 and result == True:
        print('yes')
    else:
        print('no')