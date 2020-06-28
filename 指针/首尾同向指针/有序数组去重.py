
# 方案一 切片
# from typing import List
# class Array:
#     def remove(self,num: List[int]):
#         n = len(set(num))
#         i = 0
#         while i < n-1:
#             if num[i] == num[i+1]:
#                 temp = num[i+1]
#                 num[i+1:len(num)-1] = num[i+2:]
#                 num[-1] = temp
#                 continue
#             else:
#                 i += 1
#         return i+1
# if __name__ == '__main__':
#     a = Array()
#     z = a.remove([0,0,1,1,1,2,2,3,3,4])
#     print(a.remove([0,0,1,1,1,2,2,3,3,4]))
#     print(z)

# 方案二 双指针
from typing import List
class Array:
    def remove(self,num: List[int]):
        slow = 0
        fast = 1
        while fast < len(num):
            if num[fast] == num[slow]:
                fast += 1
            else:
                slow += 1
                num[slow] = num[fast]
                fast += 1
        return slow + 1
if __name__ == '__main__':
    a = Array()
    z = a.remove([0,0,1,1,1,2,2,3,3,4])
    print(z)