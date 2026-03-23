def check(nums):
    if len(set(nums)) == 1:
        print("Все числа равны")
    elif len(set(nums)) == len(nums):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")

nums = list(map(int, input().split()))
check(nums)
