import random
import time
import sys

sys.setrecursionlimit(20000)

# -------------------------------
# INSERTION SORT
# -------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# -------------------------------
# MERGE SORT
# -------------------------------
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# -------------------------------
# QUICK SORT 
# -------------------------------
def partition(arr, low, high):
    # RANDOM PIVOT (fixes worst-case recursion issue)
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

# -------------------------------
# TIMING FUNCTION
# -------------------------------
def measure_time(sort_func, arr):
    arr_copy = arr.copy()
    start = time.time()

    if sort_func == quick_sort:
        if len(arr_copy) > 0:
            sort_func(arr_copy, 0, len(arr_copy) - 1)
    else:
        sort_func(arr_copy)

    end = time.time()
    return (end - start) * 1000  # milliseconds

# -------------------------------
# DATASET GENERATOR
# -------------------------------
def generate_datasets(size):
    random.seed(42)

    random_list = [random.randint(1, 100000) for _ in range(size)]
    sorted_list = sorted(random_list)
    reverse_list = sorted_list[::-1]

    return random_list, sorted_list, reverse_list

# -------------------------------
# MAIN FUNCTION
# -------------------------------
def main():
    sizes = [1000, 5000, 10000]

    print("Correctness Check:")
    test = [5, 2, 9, 1, 5, 6]

    print("Insertion:", insertion_sort(test.copy()))
    print("Merge:", merge_sort(test.copy()))
    print("Quick:", quick_sort(test.copy(), 0, len(test) - 1))

    print("\nPerformance Results (in ms):\n")

    for size in sizes:
        print(f"\n--- Size: {size} ---")

        random_list, sorted_list, reverse_list = generate_datasets(size)

        for name, dataset in [
            ("Random", random_list),
            ("Sorted", sorted_list),
            ("Reverse", reverse_list)
        ]:

            print(f"\n{name} Data:")

            t1 = measure_time(insertion_sort, dataset)
            t2 = measure_time(merge_sort, dataset)
            t3 = measure_time(quick_sort, dataset)

            print(f"Insertion Sort: {t1:.2f} ms")
            print(f"Merge Sort: {t2:.2f} ms")
            print(f"Quick Sort: {t3:.2f} ms")


if __name__ == "__main__":
    main()