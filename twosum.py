a = [9,4,1,7,3]
target = 10
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == target:
            print("The two numbers are:", a[i], "and", a[j])