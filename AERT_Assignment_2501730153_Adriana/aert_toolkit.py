
# Part A: Stack ADT Implementation

class StackADT:
    def __init__(self):
        self._data = []   

    def push(self, x):
        """Insert element at top of stack"""
        self._data.append(x)

    def pop(self):
        """Remove and return top element"""
        if self.is_empty():
            return "Stack is empty"
        return self._data.pop()

    def peek(self):
        """Return top element without removing"""
        if self.is_empty():
            return "Stack is empty"
        return self._data[-1]

    def is_empty(self):
        """Check if stack is empty"""
        return len(self._data) == 0

    def size(self):
        """Return number of elements in stack"""
        return len(self._data)

# Using StackADT to Store Tower of Hanoi Moves

def hanoi_with_stack(n, source, auxiliary, destination, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        stack.push(move)
        return
    
    hanoi_with_stack(n - 1, source, destination, auxiliary, stack)
    
    move = f"Move disk {n} from {source} to {destination}"
    stack.push(move)
    
    hanoi_with_stack(n - 1, auxiliary, source, destination, stack)

# Main Function for Testing Part A

if __name__ == "__main__":
    print("===== Testing Stack ADT =====")
    
    stack = StackADT()
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print("Stack size:", stack.size())
    print("Top element (peek):", stack.peek())
    print("Popped element:", stack.pop())
    print("Stack size after pop:", stack.size())
    print("Is stack empty?:", stack.is_empty())
    
    print("\n===== Using Stack to Store Tower of Hanoi Moves (N = 3) =====")
    
    hanoi_stack = StackADT()
    hanoi_with_stack(3, 'A', 'B', 'C', hanoi_stack)
    
   
    temp_stack = StackADT()
    
 
    while not hanoi_stack.is_empty():
        temp_stack.push(hanoi_stack.pop())
    
    while not temp_stack.is_empty():
        print(temp_stack.pop())



# ===============================
# Part B: Factorial & Fibonacci
# ===============================

# -------- Factorial (Recursive) --------

def factorial(n):
    """
    Recursive factorial function
    Handles n >= 0 only
    """
    if n < 0:
        return "Invalid input (factorial not defined for negative numbers)"
    
    if n == 0 or n == 1:   
        return 1
    
    return n * factorial(n - 1)


# -------- Fibonacci with Call Counters --------

naive_calls = 0
memo_calls = 0


# Naive Recursive Fibonacci
def fib_naive(n):
    global naive_calls
    naive_calls += 1
    
    if n <= 1:  
        return n
    
    return fib_naive(n - 1) + fib_naive(n - 2)


# Memoized Recursive Fibonacci (Dynamic Programming)
def fib_memo(n, memo=None):
    global memo_calls
    memo_calls += 1
    
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:  
        memo[n] = n
        return n
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# ===============================
# Testing Part B in Main
# ===============================

if __name__ == "__main__":
    
    print("\n===== PART B: FACTORIAL TESTS =====")
    
    factorial_tests = [0, 1, 5, 10]
    
    for n in factorial_tests:
        print(f"factorial({n}) =", factorial(n))
    
    
    print("\n===== PART B: FIBONACCI TESTS =====")
    
    fib_tests = [5, 10, 20, 30]
    
    for n in fib_tests:
        
        # Reset counters
        naive_calls = 0
        memo_calls = 0
        
        naive_result = fib_naive(n)
        naive_count = naive_calls
        
        memo_result = fib_memo(n)
        memo_count = memo_calls
        
        print(f"\nFibonacci n = {n}")
        print("Naive Result:", naive_result)
        print("Naive Calls:", naive_count)
        print("Memoized Result:", memo_result)
        print("Memoized Calls:", memo_count)


# ===============================
# Part C: Tower of Hanoi
# ===============================

def hanoi(n, source, auxiliary, destination):
    """
    Recursive Tower of Hanoi function
    Prints the exact sequence of moves
    """
    
    # Base Case
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Step 1: Move n-1 disks from source to auxiliary
    hanoi(n - 1, source, destination, auxiliary)
    
    # Step 2: Move nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Step 3: Move n-1 disks from auxiliary to destination
    hanoi(n - 1, auxiliary, source, destination)


# ===============================
# Testing Part C in Main
# ===============================

if __name__ == "__main__":
    
    print("\n===== PART C: TOWER OF HANOI (N = 3) =====\n")
    
    hanoi(3, 'A', 'B', 'C')


# ===============================
# Part D: Recursive Binary Search
# ===============================

def binary_search(arr, key, low, high):
    """
    Recursive Binary Search
    Returns index if found, else -1
    """
    
    # Base Case: element not found
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    # If key found
    if arr[mid] == key:
        return mid
    
    # If key is smaller, search left half
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    
    # If key is greater, search right half
    else:
        return binary_search(arr, key, mid + 1, high)


# ===============================
# Testing Part D in Main
# ===============================

if __name__ == "__main__":
    
    print("\n===== PART D: RECURSIVE BINARY SEARCH =====\n")
    
    # Required Test Case 1
    arr = [1, 3, 5, 7, 9, 11, 13]
    test_keys = [7, 1, 13, 2]
    
    print("Array:", arr)
    
    for key in test_keys:
        result = binary_search(arr, key, 0, len(arr) - 1)
        print(f"Search {key} → Index:", result)
    
    
    # Required Test Case 2 (Empty List)
    empty_arr = []
    key = 5
    
    result_empty = binary_search(empty_arr, key, 0, len(empty_arr) - 1)
    print("\nEmpty array search result:", result_empty)