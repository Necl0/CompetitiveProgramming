n = int(input())
nums = list(map(int, input().split()))

c = 0

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        c += nums[i-1] - nums[i]
        nums[i] = nums[i-1]

print(c)