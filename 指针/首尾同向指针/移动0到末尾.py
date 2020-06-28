 # 给定一个数组 nums，编写一个函数将所有0 移动到数组的末尾，同时保持非零元素的相对顺序
# 必须在原数组上操作，不能拷贝额外的数组。尽量减少操作次数。
# from typing import List
# def move(nums: List[int]):
#     f = 0
#     s = 0
#     while f < len(nums):
#         if nums[f] != 0:
#             nums[s] = nums[f]
#             s += 1
#             f += 1
#         else:
#             f += 1
#     nums[s::] = (0,)* (len(nums)-s)
#     return nums
# if __name__ == '__main__':
#     print(move([0,1,0,3,12]))

from typing import List
def movezero(nums: List[int]):
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] == 0 :
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    for i in range(slow,len(nums)):
        nums[i] = 0
    return nums
if __name__ == '__main__':
    print(movezero([0,1,0,3,12]))