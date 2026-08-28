def three_sum(nums,target):
    nums.sort()
    res = []
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == target:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    return res


a = [1,2,3,4,5,6]
b = 10
print(three_sum(a,b))