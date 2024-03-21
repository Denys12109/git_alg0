class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Bag:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
        print("Position not found in the bag")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def add_element(self, data):
        self.push(data)
        print("Position", data, "added to the stack.")

# Приклад використання:
bag = Bag()
bag.add(1)
bag.add(2)
bag.add(3)
print("Bag add position: ")
bag.display()

bag.remove(1)
print("Bag remove position: ")
bag.display()

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue: ")
queue.display()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack: ")
stack.display()

stack.add_element(4)
print("Stack add position:")
stack.display()


