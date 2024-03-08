arr = [2, 1]
size = len(arr)

smallest = 1000

for i in range(0, size):

    if arr[i] < smallest:

        smallest = arr[i]


print(smallest)

# Time complexity - O(n)


# Binary Search


def findMinInSorted(arr, size):

    start = 0
    end = size - 1

    # Check if the array is not sorted

    if arr[start] <= arr[end]:
        return arr[start]

    while start <= end:

        mid = (start + end) // 2

        # Check if the mid is the minium element
        if arr[mid] < arr[mid - 1]:
            return arr[mid]

        # If the left half is sorted the value is in right
        if arr[mid] > arr[end]:
            start = mid + 1
        else:
            end = mid - 1


output = findMinInSorted(arr, size)

print(output)


# def threeSum(arr, size):
#     arr.sort()
#     target = 24

#     for i in range(0, size-2):
#         ans = target - arr[i]
#         start = i + 1
#         end = size - 1

#         while start <= end:
#             if arr[start] + arr[end] == ans:
#                 return 1
#             elif arr[start] + arr[end] > ans:
#                 end -= 1
#             else:
#                 start += 1

#     return 0

# print(threeSum(arr, size))
