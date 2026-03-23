def make_pal(s):
    from collections import Counter
    c = Counter(s)
    mid = ""
    left = ""
    for ch, cnt in c.items():
        if cnt % 2 == 1:
            if mid != "":
                return None
            mid = ch
        left += ch * (cnt // 2)
    return left + mid + left[::-1]

s = input()
res = make_pal(s)
print(res if res else "нет информации на вывод")
