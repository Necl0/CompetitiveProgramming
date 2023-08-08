for i in range(int(input())):
    y, x = list(map(int, input().split()))
    m = max(y, x)

    d = sum([2 * i for i in range(1, m)] + [1])

    if y==x:
        print(d)
        continue
    elif m%2==1:
        print(d+x-y)
    else:
        print(d+y-x)
