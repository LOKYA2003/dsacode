arr = [3, 4, -2, 5, 8, 20, -10, 8]

def divideSub(arr):
    
    totalSum = 0

    for i in range(0, len(arr)):

        totalSum += arr[i]

    prefix = 0
    
  

    for i in range(0, len(arr) - 1):
        
        prefix += arr[i]

        ans = totalSum - prefix

        if ans == prefix:

            return 1


    return -1


print(divideSub(arr))
