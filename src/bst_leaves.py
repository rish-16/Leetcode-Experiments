class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

t1 = Node(3, Node(5, Node(6), Node(2, Node(7), Node(4))), Node(1, Node(9), Node(8)))
t2 = Node(3, Node(5, Node(6), Node(7)), Node(1, Node(4), Node(2, Node(9), Node(8))))

def get_leaves(t1, t2):
    def helper(bst, current):
        if bst is not None:
            if bst.left == None and bst.right == None: # no childer
                current.append(bst.val)
                return current
            else:
                left = helper(bst.left, current) # left is the updated `current` list
                right = helper(bst.right, left) # right is the updated `current` combined with `left`

                return right
        else:
            return current

    l1 = helper(t1, [])
    l2 = helper(t2, [])

    return l1 == l2

t1 = Node(1)
t2 = Node(2)
print (get_leaves(t1, t2))