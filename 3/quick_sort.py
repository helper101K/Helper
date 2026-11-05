import random
import time

# Deterministic Quick Sort
def partition(arr, low, high):
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
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


# Randomized Quick Sort
def randomized_quick_sort(arr, low, high):
    if low < high:

        # Select random pivot
        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]

        p = partition(arr, low, high)

        randomized_quick_sort(arr, low, p - 1)
        randomized_quick_sort(arr, p + 1, high)


# Main Program
n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

# Deterministic Quick Sort
a = arr.copy()

start = time.perf_counter()
quick_sort(a, 0, n - 1)
end = time.perf_counter()

print("\nDeterministic Quick Sort:")
print("Sorted Array:", a)
print("Execution Time:", end - start, "seconds")

# Randomized Quick Sort
b = arr.copy()

start = time.perf_counter()
randomized_quick_sort(b, 0, n - 1)
end = time.perf_counter()

print("\nRandomized Quick Sort:")
print("Sorted Array:", b)
print("Execution Time:", end - start, "seconds")

'''

Enter number of elements: 5
Enter element: 50
Enter element: 20
Enter element: 40
Enter element: 10
Enter element: 30

Deterministic Quick Sort:
Sorted Array: [10, 20, 30, 40, 50]
Execution Time: ... seconds

Randomized Quick Sort:
Sorted Array: [10, 20, 30, 40, 50]
Execution Time: ... seconds
'''