nums = list(map(int, input().split()))
K = int(input())
res = [x for x in nums if x % K == 0]
print(res)
