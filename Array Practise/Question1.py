arr = [5, 10, 20, 15]
start = 0
end = len(arr) - 1


def peakIndex(arr, start, end):

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        elif arr[mid] > arr[mid - 1]:
            start = mid + 1

        else:
            end = mid - 1
    return -1


output = peakIndex(arr, start, end)

print(output)
