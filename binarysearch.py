n=[5,3,7,9,2]
n.sort()
left=0
right=len(n)-1
target=9
while left<=right:
    mid=(left+right)//2
    if n[mid]==target:
        print("element found at index:", mid)
        break
    elif n[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print("element not found")