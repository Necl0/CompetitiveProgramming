import sys

#sys.stdin = open("triangles.in", "r"); sys.stdout = open("triangles.out", "w")

n = int(input())
points = []
m = 0
a_max = 0

for p in range(n):
    points.append(list(map(int, input().split())))

print(a_max)
