o = ["a", "b", "c"]
m1, m2 , m3 = 0, 0, 0

fin = open('shell.in', 'r')
fout = open('shell.out', 'w')

n = int(fin.readline())

for i in range(n):
    a = [int(j) for j in fin.readline().split()]

    o[a[0]-1], o[a[1]-1] = o[a[1]-1], o[a[0]-1]

    m1 += int(o[a[-1]-1]=="a")
    m2 += int(o[a[-1]-1]=="b")
    m3 += int(o[a[-1]-1]=="c")

fout.write(str(max(m1, max(m2, m3))))
fout.close()