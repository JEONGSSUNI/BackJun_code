# n개의 바구니
# m번의 도전 횟수

n, m = map(int, input().split())

n_list = [0 for i in range(n)]
m_list = []

for i in range(m) :
    m_list.append(list(map(int, input().split())))

for m_count in m_list :
    for x in range(m_count[0] - 1, m_count[1]) :
        n_list[x] = m_count[2]
for t in n_list :
    print(t, end=" ")
