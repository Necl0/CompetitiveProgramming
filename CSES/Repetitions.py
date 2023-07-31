s = input()
l = len(s)

cur = 1
m = 0

for i in range(l-1):
    if s[i] == s[i+1]:
        cur+=1
    else:
        m = max(m, cur)
        cur = 1

m = max(m, cur)
print(m)