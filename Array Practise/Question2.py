arr = [1, 423, 6, 46, 34, 23, 13, 53, 4]
size = len(arr) - 1


def maxValue(arr, size):
    largest = 0

    for i in range(0, size):
        if arr[i] > largest:
            largest = arr[i]

    return largest


def minValue(arr, size):
    smallest = arr[size]

    for i in range(0, size):
        if arr[i] < smallest:
            smallest = arr[i]

    return smallest


maximum = maxValue(arr, size)
minimum = minValue(arr, size)

print("The max element is ", maximum)
print("The min element is ", minimum)


# Another approach


a_sorted = sorted(arr)

print(a_sorted)


min = a_sorted[0]
max = a_sorted[-1]


print("The max element is ", max)
print("The min element is ", min)
