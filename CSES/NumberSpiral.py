for _ in range(int(input())):
    y, x = list(map(int, input().split()))
    m = max(y, x)
    d = m**2 - m + 1

    if y==x:
        print(d)
        continue

    print(d + x - y) if m % 2 == 1 else print(d + y - x)
