arr = [1, 2, 3, 4, 6]

n = len(arr)


sum = 0

r = n * (n + 1) // 2

for i in range(0, n - 1):

    sum += arr[i]


output = r - sum

print(output)
