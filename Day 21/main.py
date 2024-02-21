
# Segrete 0 and 1 from aray

# arr = [1, 0, 1, 0, 1, 0]

# size = len(arr)

# start = 0
# end = size - 1

# while start <= end:
#     if arr[start] == 0:
#         start += 1
#     else:
#         if arr[end] == 0:
#             # Swapping manually
#             arr[start], arr[end] = arr[end], arr[start]
#             start += 1
#             end -= 1
#         else:
#             end -= 1

# print(arr)

# Two sum problem
arr = [2, 7, 11, 15, 27]
output = []
target = 22

start = 0
end = len(arr) - 1

while start < end:
    current_sum = arr[start] + arr[end]

    if current_sum == target:
        output.append([arr[start], arr[end]])
        start += 1
        end -= 1
    elif current_sum < target:
        start += 1
    else:
        end -= 1

print(output)
