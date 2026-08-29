def find_max(a, i):
    if i == len(a) - 1:
        return a[i]

    rest = find_max(a, i + 1)

    return max(a[i], rest)

a = [3, 7, 2, 9, 5]

print(find_max(a, 0))