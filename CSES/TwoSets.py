n = int(input())
c = n*(n+1)/2

# odd cum sum
if c % 2 == 1:
    print("NO")
    quit()

t = c/2
s1, s2 = [], []
s = 0

# greedy
for b in reversed(range(1, n+1)):
    if s + b <= t:
        s1.append(b)
        s += b
    else:
        s2.append(b)


print("YES")
print(len(s1))
print(*s1)
print(len(s2))
print(*s2)