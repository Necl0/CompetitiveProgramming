n = int(input())
nums = []

if 1 < n < 4:
    print("NO SOLUTION")
    quit()

if n % 2 == 1:
    for num in reversed(range(1, n, 2)):
        nums.append(num+1)

    nums.append(n)

    for num in reversed(range(1, n-1, 2)):
        nums.append(num)
else:
    for num in range(1, n - 1, 2):
        nums.append(num+1)
    nums.append(n)

    for num in range(1, n, 2):
        nums.append(num)

print(*nums)