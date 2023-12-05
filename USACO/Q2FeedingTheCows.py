for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    o = ["."]*n
    c = 0

    for i in range(n):
        l = max(0, i-k)
        r = min(n, i+k)

        if o[l:r+1].count(s[i]) == 0:
            o[min(n-1, r)] = s[i]
            c += 1

    print(str(c) + "\n" + "".join(o))