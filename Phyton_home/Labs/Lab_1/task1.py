N = int(input())
names = input().split()
uni = []
lens = set()

for name in names:
    if len(name) not in lens:
        uni.append(name)
        lens.add(len(name))

print(names)
print(uni)
