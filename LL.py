class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


def print_list(self):
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next


def append(self, value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
    self.length += 1
    return True


def pop(self):
    if self.length == 0:
        return None
    temp = self.head
    pre = self.head
    while (temp.next):
        pre = temp
        temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -= 1
    if self.length == 0:
        self.head = None
        self.tail = None
    return temp


def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head = new_node
    self.length += 1
    return True


def pop_first(self):
    if self.length == 0:
        return None
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    if self.length == 0:
        self.tail = None
    return temp


def get(self, index):
    if index < 0 or index >= self.length:
        return None
    temp = self.head
    for _ in range(index):
        temp = temp.next
    return temp


def set_value(self, index, value):
    temp = self.get(index)
    if temp is not None:
        temp.value = value
        return True
    return False


def insert(self, index, value):
    if index > self.length or index < 0:
        return False
    # if adding to beginning
    if index == 0:
        return self.prepend(value)
    # if adding to the end
    if index == self.length:
        return self.append(value)
    new_node = Node(value)
    temp = self.get(index - 1)
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True


def remove(self, index):
    if index < 0 or index >= self.length:
        return None
    if index == 0:
        return self.pop_first()
    if index == self.length - 1:
        return self.pop()
    prev = self.get(index - 1)
    temp = prev.next
    prev.next = temp.next
    temp.next = None
    self.length -= 1
    return temp

# common interview question reverse LL


def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next
    before = None
    for _ in range(self.length):
        after = temp.next
        temp.next = before
        temp = after


def reverse(self):
    if self.length == None or self.length == 0:
        return False
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next
    before = None
    for _ in range(self.length):
        after = temp.next
        temp.next = before
        temp = after

# find the middle node in a LL


def find_middle_node(self):
    slow = self.head
    fast = self.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

# find is LL has a loop


def has_loop(self):
    slow = self.head
    fast = self.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        if fast is None:
            return False

# Find Kth Node from End


def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow

# remove duplicates from LL


def remove_duplicates(self):
    values = set()
    prev = None
    current = self.head
    while current:
        if current.value in values:
            prev.next = current.next
            self.length -= 1
        else:
            values.add(current.value)
            prev = current
            current = current.next

# Binary number to a decimal


def binary_to_decimal(self):
    num = 0
    current = self.head
    while current is not None:
        num = num * 2 + current.value
        current = current.next
    return num
