# Quick Sort Algo


# 1. Take last element as pivot
# 2. Place the pivot at its correct position
# 3. All the left elements should be smaller then the pivoit
# and all the right elements must be bigger


def partition(arr, start, end):
    pos = start

    for i in range(start, end):
        if arr[i] <= arr[end]:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1

    arr[pos], arr[end] = arr[end], arr[pos]
    return pos


def quickSort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)

        # Recursively sort the subarrays
        quickSort(arr, start, pivot - 1)
        quickSort(arr, pivot + 1, end)


arr = [10, 80, 90, 20, 30]
start = 0
end = len(arr) - 1

quickSort(arr, start, end)

print(arr)
