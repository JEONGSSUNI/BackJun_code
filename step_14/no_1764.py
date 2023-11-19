import sys
n, m = map(int, input().split())

n_set = set()
for i in range(n) :
    n_set.add(sys.stdin.readline().rstrip())

m_set = set()

for j in range(m) :
    name = sys.stdin.readline().rstrip()
    if name in n_set :
        m_set.add(name)

m_set = sorted(m_set)

print(len(m_set))
for nn in m_set :
    print(nn)