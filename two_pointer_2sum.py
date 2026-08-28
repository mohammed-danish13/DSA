def twopointer(nums, target):
    left,right = 0,len(nums)-1
    
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left,right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return None

nums = [1,3,4,7,9]
target = 10
print(twopointer(nums,target))