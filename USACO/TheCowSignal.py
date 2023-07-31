#fin = open('cowsignal.in', 'r')
#fout = open('cowsignal.out', 'w')

m, n, k = [int(i) for i in input().split()]

symbol = ''
for j in range(m):
    symbol += input() + "\n"

end = ''
for a in range(k*m):
    for char in symbol.split("\n")[a//2]:
        end += char*k
    end += '\n'

print(end)
#fout.write(end)
#fout.close()