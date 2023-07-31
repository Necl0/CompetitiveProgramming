import sys

#sys.stdin = open("balancing.in", "r"); sys.stdout = open("balancing.out", "w")

n, b = list(map(int, input().split()))
p = []

for case in range(n):
    p.append(list(map(int, input().split())))

x_vals = [pair[0] for pair in sorted(p, key=lambda p:p[0])]
y_vals = [pair[1] for pair in sorted(p, key=lambda p:p[1])]

# brute force
min_m = float('inf')

for x_part in range(0, x_vals[-1], 2):
    for y_part in range(0, y_vals[-1], 2):
        q = [0] * 4

        for point in p:
            x = point[0]
            y = point[1]

            # top left
            if x < x_part and y > y_part:
                q[0] += 1

            # top right
            elif x > x_part and y > y_part:
                q[1] += 1

            # bottom left
            if x < x_part and y < y_part:
                q[2] += 1

            # bottom right
            elif x > x_part and y < y_part:
                q[3] += 1

        min_m = min(min_m, max(q))


print(min_m)
