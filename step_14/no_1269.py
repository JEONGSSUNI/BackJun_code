import sys
n, m = map(int, sys.stdin.readline().split())

set_a = set(map(int, sys.stdin.readline().split()))
set_b = set(map(int, sys.stdin.readline().split()))

first_len = len(set_a - set_b)
second_len = len(set_b - set_a)

print(first_len + second_len)