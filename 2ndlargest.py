def secondlargest(arr):
    first = arr[0]
    second = arr[0]
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != arr[0] else None
print(secondlargest([1, 2, 3, 4, 5]))
