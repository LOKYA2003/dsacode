
# Find first and last position 
# Find missing number position

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
start = 0
end = len(arr) - 1
target = 3


def searchInSorted(arr, start, end):
     
    while start <= end:
        mid  = (start+end)//2

    # Left hand side
    if arr[mid] == target:
        return mid
    elif arr[mid]>=arr[0]:
        if arr[start]<=target and arr[mid] > target:
            end = mid - 1
        else 
            start = mid+1
    
    
            


      


output =  searchInSorted(arr, start, end)

print("Search In Sorted",arr[output])
