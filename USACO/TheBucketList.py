fin = open('blist.in', 'r')
fout = open('blist.out', 'w')


n = int(fin.readline())
m = 0
c = []

for i in range(n):
    entry = [int(a) for a in fin.readline().split()]
    c += [entry]
    s, t, b = entry

c = sorted(c, key=lambda x: x[0])

for i in range(1000):
    t = 0
    for cow in c:
        if cow[0] <= i <= cow[1]:
            t += cow[-1]

    m = max(m, t)

fout.write(str(m))
fout.close()
