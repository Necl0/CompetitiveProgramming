i = input()
s = list(set(i))
f = []
h = ""

a = [i.count(letter) for letter in s]
odds = [l for l in s if i.count(l) % 2 == 1]

if len(odds) == 0:
    st = ""

    for i in range(len(s)):
        st += s[i] * int(a[i] / 2)

    print(st + st[::-1])
elif len(odds) == 1:
    for letter in s:
        c = i.count(letter)

        if c % 2 == 0:
            f += [letter] * int(c / 2)
        elif s.count(letter) % 2 == 1:
            h = letter

    print("".join(f + [h] * i.count(h) + list(reversed(f))))
else:
    print("NO SOLUTION")