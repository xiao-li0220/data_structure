# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

# 傻瓜法
# def twosum(nums,target):
#     i = 0
#     j = 1
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i] + nums[j] == target:
#                 return i,j
#
# if __name__ == '__main__':
#     a = twosum([1,2,5,11,13,15],15)
#     print(a)


# 字典存放
# def twosum(nums,target):
#     nums_dict = {}
#     for i in range(len(nums)):
#         temp = target - nums[i]
#         if temp in nums_dict:
#             return [i,nums_dict[temp]]
#         else:
#             nums_dict[nums[i]] = i
# if __name__ == '__main__':
#     list = [1,2,5,11,13,15]
#     print(twosum(list,15))


# 对撞指针
from typing import List
def twoSum(nums: List,target: int):
    left = 0
    right = len(nums)-1
    while left < right:
        curr = nums[left] + nums[right]
        if  curr == target:
            print(nums[left],nums[right])
            return left,right
            left += 1
            right -= 1
        else:
            if curr < target:
                left += 1
            else:
                right -= 1
print(twoSum([1,2,5,11,13,15],15))

