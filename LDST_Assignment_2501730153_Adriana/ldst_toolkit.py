# ------------------------------
# Dynamic Array Implementation
# ------------------------------
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self._resize()

        self.arr[self.size] = x
        self.size += 1
        print(f"Appended {x} | Size: {self.size}, Capacity: {self.capacity}")

    def _resize(self):
        print("Resizing...")
        self.capacity *= 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def pop(self):
        if self.size == 0:
            return "Array is empty"
        val = self.arr[self.size - 1]
        self.size -= 1
        print(f"Popped {val}")
        return val

    def display(self):
        print(self.arr[:self.size])


# ------------------------------
# Singly Linked List
# ------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_value(self, x):
        temp = self.head

        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ------------------------------
# Doubly Linked List
# ------------------------------
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new_node = DNode(x)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_after(self, target, x):
        temp = self.head
        while temp:
            if temp.data == target:
                new_node = DNode(x)
                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node
                return
            temp = temp.next

    def delete_position(self, pos):
        if not self.head:
            return

        temp = self.head

        for _ in range(pos):
            if not temp:
                return
            temp = temp.next

        if not temp:
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# ------------------------------
# Stack using Linked List
# ------------------------------
class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            return "Stack Underflow"
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if not self.head:
            return "Empty"
        return self.head.data


# ------------------------------
# Queue using Linked List
# ------------------------------
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return "Queue Underflow"
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        if not self.head:
            return "Empty"
        return self.head.data


# ------------------------------
# Parentheses Checker
# ------------------------------
def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.pop() != pairs[ch]:
                return False

    return stack.head is None


# ------------------------------
# MAIN TEST RUNNER
# ------------------------------
if __name__ == "__main__":
    print("\n--- Dynamic Array ---")
    da = DynamicArray()
    for i in range(10):
        da.append(i)
    da.display()
    da.pop()
    da.pop()
    da.pop()
    da.display()

    print("\n--- Singly Linked List ---")
    sll = SinglyLinkedList()
    sll.insert_beginning(3)
    sll.insert_beginning(2)
    sll.insert_beginning(1)
    sll.insert_end(4)
    sll.insert_end(5)
    sll.traverse()
    sll.delete_value(3)
    sll.traverse()

    print("\n--- Doubly Linked List ---")
    dll = DoublyLinkedList()
    for i in range(1, 6):
        dll.insert_end(i)
    dll.insert_after(3, 99)
    dll.traverse()
    dll.delete_position(1)
    dll.delete_position(4)
    dll.traverse()

    print("\n--- Stack ---")
    st = Stack()
    st.push(10)
    st.push(20)
    print(st.pop(), st.peek())

    print("\n--- Queue ---")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue(), q.front())

    print("\n--- Parentheses Checker ---")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(t, "->", is_balanced(t))