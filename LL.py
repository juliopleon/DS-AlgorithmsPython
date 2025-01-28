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
        new_node = self.head
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
