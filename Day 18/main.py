
# Find first and last position 
# Find missing number position

arr = [2,4,6,7,8,9]
start = 0
end = len(arr) - 1
target = 5

def findPosi(arr, start, end, target):
    index = len(arr)
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
           index = mid
           break
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            index = mid

    return index

output =  findPosi(arr, start, end, target)

print("Target Posi",output)



# Find first and last position 
# Find missing number position

arr = [2,4,8,8,8,9]
start = 0
end = len(arr) - 1
target = 8

def firstPosition(arr, start, end, target):
    first = -1    
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            first = mid
            end = start - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return first




def lastPosition(arr, start, end, target):
    last = -1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            last = mid
            start = start + 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return last

first =  firstPosition(arr, start, end, target)
last =  lastPosition(arr, start, end, target)

print("First",first)
print("Last",last)
