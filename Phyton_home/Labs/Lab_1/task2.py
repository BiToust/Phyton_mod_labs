import math
N = int(input())
nums = list(range(N, N*N + 1))
roots = [math.sqrt(x) for x in nums]
print(nums)
print(roots)
