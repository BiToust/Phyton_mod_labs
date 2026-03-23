class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None

class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            return None
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        node = Node(val)
        node.pref = self.end
        self.end = node

    def print(self):
        cur = self.end
        while cur:
            print(cur.data)
            cur = cur.pref


# --- ТЕСТ, чтобы показать, что стек работает ---
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Стек после push:")
s.print()

print("pop:", s.pop())

print("Стек после pop:")
s.print()
