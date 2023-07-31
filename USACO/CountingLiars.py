n = int(input())
m = n
f = []

for entry in range(n):
    d, l = list(input().split())
    f.append([d, int(l)])


for loc in range(max(sorted(f, key=lambda x: x[1]))[1]):
    lies = 0
    for val in f:
        if val[0] == 'G' and val[1] > loc:
            lies+=1
        elif val[0] == 'L' and val[1] < loc:
            lies+=1

    m = min(m, lies)

print(m)


