# from typing import List
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         slow = 0
#         fast = 0
#         while fast < len(nums):
#             if nums[fast] == val:
#                 fast += 1
#             else:
#                 nums[slow] = nums[fast]
#                 slow += 1
#                 fast += 1
#         return slow
# if __name__ == '__main__':
#     a = Solution()
#     print(a.removeElement([0,1,2,2,3,0,4,2],2))
#
# # from typing import List
# # class Solution:
# #     def removeElement(self, nums: List[int], val: int) -> int:
# #         slow = 0
# #         fast = 0
# #         while fast < len(nums):
# #             if nums[fast] != val:
# #                 nums[slow] = nums[fast]
# #                 slow += 1
# #                 fast += 1
# #             else:
# #                 fast += 1
# #         return slow