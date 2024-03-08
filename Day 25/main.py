arr = [12, 3, 4, 1, 6, 9]
size = len(arr)

def threeSum(arr, size):
    arr.sort()
    target = 24

    for i in range(0, size-2):
        ans = target - arr[i]
        start = i + 1
        end = size - 1

        while start <= end:
            if arr[start] + arr[end] == ans:
                return 1
            elif arr[start] + arr[end] > ans:
                end -= 1
            else:
                start += 1

    return 0

print(threeSum(arr, size))
