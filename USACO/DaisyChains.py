n = int(input())
f = list(map(int, input().split()))
c = 0

for seq_s in range(n):
    for seq_end in range(n):
        if seq_s <= seq_end:
            seq = f[seq_s: seq_end+1]
            if sum(seq)/len(seq) in seq:
                c += 1

print(c)