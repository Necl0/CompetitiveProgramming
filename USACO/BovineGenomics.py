import sys

sys.stdin = open("cownomics.in", "r"); sys.stdout = open("cownomics.out", "w")

n, m = list(map(int, input().split()))

data = [[], []]
p = m

for cow in range(n):
    data[0].append(input())

for cow in range(n):
    data[1].append(input())

for pos in range(m):
    for value in set([data[0][i][pos] for i in range(n)]):
        if value in set([data[1][i][pos] for i in range(n)]):
            p-=1
            break

print(p)
