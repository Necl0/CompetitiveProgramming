n = int(input())

x = [int(a) for a in input().split()]
y = [int(b) for b in input().split()]

max_e = 0

for i in range(len(x)):
    for j in range(len(y)):
        max_e = max(max_e, (x[i]-x[j])**2 + (y[i]-y[j])**2)

print(max_e)