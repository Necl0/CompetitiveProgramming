import sys

#sys.stdin = open("diamond.in", "r"); sys.stdout = open("diamond.out", "w")

n, k = list(map(int, input().split()))

d = [0] * n
m = 0

for i in range(n):
    d[i] = int(input())

for seq_s in range(n):
    for seq_end in range(n):
        if seq_s < seq_end:
            seq = sorted(d[seq_s: seq_end+1])
            print(seq)
            if max(seq) - min(seq) < k:
                m = len(seq)

print(m)