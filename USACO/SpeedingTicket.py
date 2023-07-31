fin = open('speeding.in', 'r')
fout = open('speeding.out', 'w')

n, m = [int(a) for a in fin.readline().split()]
acceptable = []
bessie_speed = []
z = 0

for i in range(n):
    length, lim = [int(j) for j in fin.readline().split()]
    acceptable += [lim] * length

for x in range(m):
    length_b, lim_b = [int(y) for y in fin.readline().split()]
    bessie_speed += [lim_b] * length_b

for i in range(100):
    z = max(z, bessie_speed[i] - acceptable[i])

fout.write(str(z))
fout.close()


