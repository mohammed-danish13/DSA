n=int(input("Enter the number : "))
a=[]
for i in range(n):
    a.append(int(input()))
key=int(input("enter key:"))
for i in range(n):
    if a[i]==key:
        print("key found at index",i)
        break
else:
        print("key not found")