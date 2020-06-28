# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

from typing import List
def twoSum(nums: List[int],target: int):
    n1 = nums[:]
    n2 = n1[::-1]
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            break
        else:
            if curr < target:
                left += 1
            else:
                right -= 1
    x = n1.index(nums[left])
    y = (len(n2)-1) - n2.index(nums[right])
    if x < y:
        return [x,y]
    else:
        return [y,x]
nums=[11,2,15,7]
print(twoSum(nums,9))