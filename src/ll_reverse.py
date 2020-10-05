class Node: 
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class Stack:
    def __init__(self):
        self.mem = []

    def add(self, v):
        self.mem = [v] + self.mem

    def pop(self):
        v = self.mem[0]
        self.mem = self.mem[1:]
        return v

def reverse(xs):
    s = Stack()

    def helper(L):
        if L is None:
            pass
        else:
            cur = L.val
            s.add(cur) # store in stack
            helper(L.nxt)
    helper(xs)

    def create(prev):
        if len(s.mem) > 0:
            v = s.pop()
            node = Node(v)
            prev.nxt = node
        
            return create(node)
        else:
            return prev

    head = s.pop()
    newnode = Node(head)
    res = create(newnode)
    
    return newnode

l1 = Node(1, nxt=Node(2, nxt=Node(3, nxt=Node(4, nxt=Node(5)))))
l2 = reverse(l1)

def traverse(l):
    if l is None:
        return ""
    else:
        return "{}".format(l.val) + traverse(l.nxt)

print (traverse(l1))
print (traverse(l2))