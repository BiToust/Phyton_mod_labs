class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.start is None:
            return None
        val = self.start.data
        self.start = self.start.nref
        if self.start:
            self.start.pref = None
        else:
            self.end = None
        return val

    def push(self, val):
        node = Node(val)
        if self.end is None:
            self.start = self.end = node
        else:
            self.end.nref = node
            node.pref = self.end
            self.end = node

    def insert(self, n, val):
        if n == 0:
            node = Node(val)
            node.nref = self.start
            if self.start:
                self.start.pref = node
            self.start = node
            if self.end is None:
                self.end = node
            return

        cur = self.start
        i = 0
        while cur and i < n - 1:
            cur = cur.nref
            i += 1

        if cur is None:
            return

        node = Node(val)
        node.nref = cur.nref
        node.pref = cur
        if cur.nref:
            cur.nref.pref = node
        else:
            self.end = node
        cur.nref = node

    def print(self):
        cur = self.start
        while cur:
            print(cur.data)
            cur = cur.nref


# --- ТЕСТ, чтобы показать, что очередь работает ---
q = Queue()
q.push(10)
q.push(20)
q.push(30)

print("Очередь после push:")
q.print()

print("pop:", q.pop())

print("Очередь после pop:")
q.print()

q.insert(1, 99)
print("Очередь после insert(1, 99):")
q.print()
