arr = [10, 80, 30, 90, 40]

n = len(arr)

for i in range(0, n - 1):

    for j in range(i + 1, n):

        if arr[j] < arr[i]:

            arr[i] = arr[j]


print(arr)

# dupli = []

# for i in range(0, n - 1):

#     for j in range(i + 1, n):

#         if arr[i] == arr[j]:

#             dupli.insert(0, arr[i])
#             break

# print(dupli)
