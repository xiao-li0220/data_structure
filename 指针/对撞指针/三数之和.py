# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
#
# 思路:给数组排序后,固定一个C位,从他的右边使用对撞指针,优化:去重C位和俩个指针数字
from typing import List
def threeSum(nums :List[int]):
    nums.sort()
    result = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] < 0:
                left += 1
            elif nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            else:
                result.append([nums[i],nums[left],nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return result
nums = [-1,0,1,2,3,4,1,-1,-2]
print(threeSum(nums))