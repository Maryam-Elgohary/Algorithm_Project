# Heapify function to maintain the max-heap property
def heapify(arr, n, i):
    """
    Ensures the subtree rooted at index 'i' satisfies the Max-Heap property.

    Parameters:
    arr -- list to heapify
    n -- size of the heap
    i -- index to maintain the heap property for
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if the left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if the right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

# Function to build a max heap from the input list
def build_max_heap(arr):
    """
    Transforms a list into a Max-Heap.

    Parameters:
    arr -- list to transform into a Max-Heap
    """
    n = len(arr)
    # Start from the last non-leaf node and go up to the root
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# Main Heap-Sort function
def heap_sort(arr):
    """
    Sorts a list using Heap-Sort.

    Parameters:
    arr -- the list to sort

    Returns:
    arr -- the sorted list
    """
    n = len(arr)

    # Step 1: Build a max heap
    build_max_heap(arr)

    # Step 2: Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Swap the root (maximum element) with the last element in the current heap
        arr[i], arr[0] = arr[0], arr[i]
        # Reduce the size of the heap and heapify the root
        heapify(arr, i, 0)

    return arr

# Example usage
if __name__ == "__main__":
    # Input sequence of numbers
    numbers = [12, 11, 13, 5, 6, 7]
    print("Original Array:", numbers)

    # Perform Heap-Sort
    sorted_numbers = heap_sort(numbers)
    print("Sorted Array:", sorted_numbers)
