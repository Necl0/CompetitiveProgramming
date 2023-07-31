for _ in range(int(input())):
    a, b = map(int, input().split())
    if (a == b and a % 3 == 0) or (a >= b//2 and b >= a//2 and a != 0 and b != 0 and (a + b) % 3 == 0):
        print("YES")
    else:
        print("NO")
