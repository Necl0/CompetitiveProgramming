n = int(input())
nums = set(map(int, input().split()))

for num in range(1, n+1):
    if num not in nums:
        print(num)
        exit()
