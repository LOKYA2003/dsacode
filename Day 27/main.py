
# Three sum problem 


arr = [12,3,4,1,6,9]

target = 24

size = len(arr)


# Brute force approach

# def threeSum(arr,size,target):
     
#     for i in range(0,size-2):
        
#         for j in range(i+1,size-1):
            
#             for k in range(j+1,size):
                
#                 if arr[i] + arr[j] + arr[k] == target:
                    
#                     print(arr[i],arr[j],arr[k])
                    
#                     return 1
                
#     return 0


# threeSum(arr,size,target)


# Optimial Approach


def threeSum(arr,size,target):
     
    arr.sort()
    for i in range(0,size-2):
        
        
        start = i+1
        end = size - 1
        
        
        while(start<=end):
            
            if( arr[i] + arr[start] + arr[end] == target):
                    print("Triplet is", arr[i], 
                        ', ', arr[start], ', ', arr[end])
                    return True
                
            elif (arr[i] + arr[start] + arr[end] < sum):
                    start += 1
            else: 
                    end -= 1
       
       
       
       


threeSum(arr,size,target)