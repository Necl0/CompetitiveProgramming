import sys

sys.stdin = open("pails.in", "r"); sys.stdout = open("pails.out", "w")

x, y, m = map(int, input().split())

max_m = 0
a = m//x

for a_val in range(1, a+1):
    for y_count in range(a_val):
        combo = (a_val-y_count)*x + y_count*y
        if m>=combo>max_m:
            max_m = combo

print(max_m)


