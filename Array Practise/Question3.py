# Sort the array of 0 1 and 2


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

size = len(arr) - 1


# Dutch National Flag Algo


low = 0
mid = 0
high = size

while mid <= high:

    if arr[mid] == 0:
        arr[mid], arr[low] = arr[low], arr[mid]
        low += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1


print(arr)
