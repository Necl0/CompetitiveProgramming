import sys

#sys.stdin = open("gymnastics.in", "r"); sys.stdout = open("gymnastics.out", "w")

k, n = list(map(int, input().split()))
data = []
c = 0

for i in range(k):
    data.append(list(map(int, input().split())))

# pairs
for c1 in range(1, n+1):
    for c2 in range(1, n+1):
        c += 1 if [sess.index(c1) < sess.index(c2) for sess in data] == [data[0].index(c1) < data[0].index(c2)] * k and c1 != c2 else 0

print(int(c/2))