# delete a node in linked list at index k
def delete(head, k):
    if head is None:
        return
    curr = head
    if k == 0:
        head = curr.next
        curr = None
    for i in range(k - 1):
        curr = curr.next
        if curr is None:
            return
    if curr.next is None:
        return
    temp = curr.next.next
    curr.next = None
    curr.next = temp


# insert a node in linked list at index k with data
def insert(head, k, data):
    new_node = Node(data)
    curr = head
    if k == 0:
        new_node.next = hea
        head = new_node
    for i in range(k - 1):
        curr = curr.next
        if curr is None:
            return
    temp = curr.next
    curr.next = new_node
    new_node.next = temp


# reverse a linked list
def reverse(head):
    if head is None:
        return
    curr = head
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev


# reverse half of a linked list
def reverse_half(head):
    if head is None:
        return
    curr = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = curr
        curr = curr.next
        fast = fast.next.next
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        temp = curr.next
    head = prev

# stack which stores minimum and maximum value


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def length(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]


class Stack_min_max:
    def __init__(self):
        self.items = Stack()
        self.max = Stack()
        self.min = Stack()

    def push_min_max(self, item):
        if is_empty(self.max) or peek(self.max) < item:
            push(self.max, item)
        if is_empty(self.min) or peek(self.min) > item:
            push(self.min, item)
        return push(self.items, i)

    def pop_min_max(self):
        if peek(self.items) == peek(self.max):
            pop(self.max)
        if peek(self.items) == peek(self.min):
            pop(self.min)
        return pop(self.items)

    def give_max(self):
        return peek(self.max)

    def give_min(self):
        return peek(self.min)


# find a value in the tree. return False if it doesn't exist.
def find_value(root, val):
    while root:
        if root.val == val:
            return root
        if root.val > val:
            root = root.left
        else:
            root = root.right
    return False

# level order tree traversal


def level_order(root):
    if root is None:
        return
    queue = [root]
    while queue:
        curr = queue.pop(0)
        print(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

# max sum of contigous subarray


def max_sum(arr):
    if not arr:
        return 0
    current_sum = A[0]
    max_sum = A[0]
    for num in A[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# merge two sorted arrays


def merge_arrays(arr1, arr2):
    merged_array = []
    length1 = len(arr1)
    length2 = len(arr2)
    while(i < length1 or j < length2):
        if i > length2:
            merged_array.append(arr[i])
            i += 1
        elif j > length1:
            merged_array.append(arr[j])
            j += 1
        elif arr[i] > arr[j]:
            merged_array.append(arr[i])
            i += 1
        else:
            merged_array.append(arr[j])
            j += 1

    return merged_array

# determine if BT is BST


def validate_BST(node):
    if node is None:
        return True
    stack = [node]
    while stack:
        curr = stack.pop()
        if curr.left:
            if curr.val > curr.left.val:
                return False
            else:
                stack.append(curr.left)
        if curr.right:
            if curr.val < curr.right.val:
                return False
            else:
                stack.append(curr.right)
     return True

# two sum problem
def two_sum(arr, k):
    complements = set()
    for num in arr:
        if num in complements:
            return True
        else:
            complements.add(k - num)
    return False
         
# nth fibonacci number (baaad)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# nth fibonacci number (efficient)
def fib(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(n,2):
            c = a+b
            a = b
            b = c
        return b
    
def lowest_common_ancestor(node, n1, n2):
    path_n1 = []
    path_n2 = []
    
    if not path_exists(node, n1, path_n1) or not path_exists(node, n2, path_n2):
        return False
    while i < len(path_n1) and i < len(path_n2):
        if path_n1[i] == path_n2[i]:
            return path_n1[i - 1]
        i += 1

def path_exists(node, n, path):
    if node is None:
        return False
    path.append(node.key)
    if node.key == n:
        return True
    if ((node.left and path_exists(node.lef, n, path)) or (node.right and path_exists(node.right, n, path))):
        return True
    path.pop()
    return False

# DONE------lowest common ancestor (first common ancestor)     
# tree serialize and deserialize -> literally just printing all values AND NULLS in a bfs
# train platforms (process two arrays)
# intersection of two linkedlists
# to-do: Deep Copy random linkedlist
# overlap of two rectangles given top-right/bottom-left coordinates
# implement a hash table
# distance between two nodes in BST
# 2D-matrix type problems (like Redfin) (CONNECTED COMPONENT LABELLING)
# duplicate element in linkedlist/cycle (slownode, fastnode)
# DONE----single number (bit operations) 
# how does grep work?
# implement mergesort, quicksort
# DONE-------merge two sorted arrays (lockstep)
# DONE-------determine if bt is a BST
# DONE------nth fibonacci number(DP)
# DONE------2sum problem

# QUICKLY REVIEW TRADEOFFS of ARRAY vs. LinkedLists, STACK vs. QUEUE, HASH TABLE
# QUICKLY REVIEW OOP STUFF
