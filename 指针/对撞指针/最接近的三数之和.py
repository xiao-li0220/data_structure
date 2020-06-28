from typing import List
def threeSumCloest(nums: List[int],target: int) -> int:
    nums.sort()
    min = abs(nums[0] + nums[1] + nums[2] - target)
    sums = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):
        left = i + 1
        right = len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if abs(sum-target) < min:
                min = abs(sum-target)
                sums = sum
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return (sum)
    return sums
    # return (sums,[nums[i],nums[left],nums[right]])
nums = [-1,0,2,1]
print(threeSumCloest(nums,1))
# 返回数值有问题
