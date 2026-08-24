a=[5,3,7,2,4]
k = 3
window_sum = sum(a[:k])
max_sum = window_sum

for i in range(k, len(a)):
    window_sum = window_sum - a[i-k] + a[i]
    max_sum = max(max_sum, window_sum)

print("Maximum sum of a subarray of size", k, "is:", max_sum)
