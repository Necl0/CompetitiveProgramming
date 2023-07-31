import sys

sys.stdin = open("lifeguards.in", "r"); sys.stdout = open("lifeguards.out", "w")

n = int(input())
data = []
m = 0

for i in range(n):
    data.append(list(map(int, input().split())))


for lg in data:
    c = 0
    # see how much is covered without it
    for time in range(1001):
        for g in data:
            # other guards
            if g != lg and g[0] < time <= g[1]:
                c += 1
                break

    m = max(m, c)

print(m)


