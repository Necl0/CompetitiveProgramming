import sys, itertools

sys.stdin = open("circlecross.in", "r"); sys.stdout = open("circlecross.out", "w")

s = input()
c = 0

# generate pairs of letters
pairs = list(itertools.permutations("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 2))

for pair in pairs:
    if s.find(pair[0]) < s.find(pair[1]) < s.find(pair[0], s.find(pair[0])+1) < s.find(pair[1], s.find(pair[1])+1):
        c+=1

print(c)
