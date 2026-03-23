prices = list(map(int, input().split()))
K = int(input())
M = int(input())

discount = [p - (p // K) * M for p in prices]

print(prices)
print(discount)
