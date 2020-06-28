from typing import List
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    nums_set = set()
    i,j = 0,0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            nums_set.add(nums1[i])
            i += 1
            j += 1
    return list(nums_set)
nums1 = [4,9,5]
nums2 = [4,8,4,9,9,1]
print(intersection(nums1,nums2))