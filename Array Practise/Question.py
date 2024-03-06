# Count Pairs with the given sum

# 1. I used two pointer approch over here
# the main thing was using the pattern. Or what we can say,
# I looked at the pattern, and I came on this approach,
# where we can use 2 pointers and solve this problem.
# The time complexity of this problem is B go of N Square.

arr = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]

k = 6
size = len(arr)
target = 11
count = 0

for i in range(0, size):

    for j in range(i + 1, size):

        if arr[i] + arr[j] == target:

            count += 1


print("Pair Sum Values Are :", count)
