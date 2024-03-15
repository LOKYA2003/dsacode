
# Array
# arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]

# n = len(arr)

# Brute force app

# Sort the array

# arr.sort()

# arr.reverse()

# print(arr)

#Optimal App

# start = 0
# end = n - 1

# while start <= end:
#     if arr[start] == 0:
#         if arr[end] != 0:
#             arr[start], arr[end] = arr[end], arr[start]
#         end -= 1
#     else:
#         start += 1

# print(arr)


#  2D array

w, h = 4, 3
Matrix = [[0 for x in range(w)] for y in range(h)] 

print(Matrix)