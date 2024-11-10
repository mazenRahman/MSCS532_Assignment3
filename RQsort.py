import random

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]  # Swap pivot to end
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
import random

# Example arrays to test the function
random_array = [random.randint(0, 100) for _ in range(10)]  # Randomly generated array
sorted_array = list(range(10))                              # Already sorted array
reverse_sorted_array = list(range(10, 0, -1))               # Reverse-sorted array
repeated_elements_array = [5] * 10                          # Array with repeated elements

# Define low and high indices
low = 0
high = len(random_array) - 1

# Test with each example array
print("Original Random Array:", random_array)
randomized_quicksort(random_array, low, high)
print("Sorted Random Array:", random_array)

print("\nOriginal Sorted Array:", sorted_array)
randomized_quicksort(sorted_array, low, len(sorted_array) - 1)
print("Sorted Sorted Array:", sorted_array)

print("\nOriginal Reverse-Sorted Array:", reverse_sorted_array)
randomized_quicksort(reverse_sorted_array, low, len(reverse_sorted_array) - 1)
print("Sorted Reverse-Sorted Array:", reverse_sorted_array)

print("\nOriginal Repeated Elements Array:", repeated_elements_array)
randomized_quicksort(repeated_elements_array, low, len(repeated_elements_array) - 1)
print("Sorted Repeated Elements Array:", repeated_elements_array)
