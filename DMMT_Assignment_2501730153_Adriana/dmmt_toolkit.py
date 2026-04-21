# ---------------- BST IMPLEMENTATION ----------------
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Case 1: No child
            if node.left is None and node.right is None:
                return None
            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Case 3: Two children
            successor = self._min_value(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        return node

    def _min_value(self, node):
        while node.left:
            node = node.left
        return node

# ---------------- GRAPH IMPLEMENTATION ----------------
from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, w):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append((v, w))

    def print_graph(self):
        for node in self.adj:
            print(node, "->", self.adj[node])

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        order = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                for neighbor, _ in self.adj.get(node, []):
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        visited = set()
        order = []
        self._dfs(start, visited, order)
        return order

    def _dfs(self, node, visited, order):
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor, _ in self.adj.get(node, []):
                self._dfs(neighbor, visited, order)

# ---------------- HASH TABLE IMPLEMENTATION ----------------
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(i, "->", bucket)

# ---------------- MAIN TEST RUNNER ----------------
if __name__ == "__main__":
    print("===== BST TEST =====")
    bst = BST()
    nums = [50, 30, 70, 20, 40, 60, 80]
    for n in nums:
        bst.insert(n)

    print("Inorder:", bst.inorder())
    print("Search 20:", bst.search(20))
    print("Search 90:", bst.search(90))

    bst.delete(20)
    print("After deleting leaf (20):", bst.inorder())

    bst.insert(65)
    bst.delete(60)
    print("After deleting one-child (60):", bst.inorder())

    bst.delete(50)
    print("After deleting two-child (50):", bst.inorder())

    print("\n===== GRAPH TEST =====")
    g = Graph()
    edges = [
        ('A','B',2), ('A','C',4), ('B','D',7), ('B','E',3),
        ('C','E',1), ('D','F',5), ('E','D',2), ('E','F',6), ('C','F',8)
    ]

    for u,v,w in edges:
        g.add_edge(u,v,w)

    print("Adjacency List:")
    g.print_graph()

    print("BFS from A:", g.bfs('A'))
    print("DFS from A:", g.dfs('A'))

    print("\n===== HASH TABLE TEST =====")
    ht = HashTable(5)

    keys = [10, 15, 20, 7, 12]
    for k in keys:
        ht.insert(k, k*10)

    print("Hash Table:")
    ht.display()

    print("Get 10:", ht.get(10))
    print("Get 15:", ht.get(15))
    print("Get 7:", ht.get(7))

    ht.delete(15)
    print("After deleting 15:")
    ht.display()
