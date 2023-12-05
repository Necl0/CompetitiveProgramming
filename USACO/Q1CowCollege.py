n = int(input())
l = list(sorted(list(map(int, input().split()))))

m_t = 0
m_c = float('inf')

for i in reversed(range(len(l))):
    t = l[i] * (n-i)

    if t >= m_t:
        m_t = t
        m_c = l[i]

print(m_t, m_c)