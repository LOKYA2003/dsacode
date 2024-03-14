# Find the second largest value from the array
# 'Lucida Console',
arr = [4, 5, 3, 6, 7]

size = len(arr)

# Brute Force

# def secondLargest(arr,size):

#     arr.sort()

#     secondLargestValue = 0

#     secondLargestValue = arr[size-2]

#     return secondLargestValue


# output = secondLargest(arr,size)


# print(output)

# Time complexity = O(n log n)


# Improved Approach


# 1. Largest value
# 2. Second loop mein largest ko chod kar sabh check
# 3. I once again traverse and get the higest value


def secondLargest(arr, size):
    if (size < 2):
        return -1
    large = float('-inf')
    second_large = float('-inf')

    for i in range(size):
        if arr[i] > large:
            second_large = large
            large = arr[i]
        elif arr[i] > second_large and arr[i] != large:
            second_large = arr[i]

    return second_large



def secondSmallest(arr, size):
    if (size < 2):
        return -1
    small = float('inf')
    second_small = float('inf')

    for i in range(size):
        if arr[i] < small:
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and arr[i] != small:
            second_small = arr[i]

    
    return second_small

print(secondSmallest(arr, size))

