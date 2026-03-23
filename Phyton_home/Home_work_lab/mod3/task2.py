n=input()
print("Неверный ввод") if not n.isdigit() or n=="0" else print(f"{bin(int(n))[2:]}, {oct(int(n))[2:]}, {hex(int(n))[2:].upper()}")
