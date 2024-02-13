
# Find first and last position 
# Find missing number position

arr = [2,4,6,8,10,81,5]
start = 0
end = len(arr) - 1
target = 5


def highestPeak(arr, start, end):
     
    while start <= end:
        mid  = (start+end)//2

        if(arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]):
            return mid
        elif(arr[mid] > arr[mid-1]):
            start = mid + 1
        else:
            end = mid  - 1
            
    return mid

      


output =  highestPeak(arr, start, end)

print("Highest Peak",arr[output])
