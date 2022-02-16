from statistics import median
from typing import List


nums1 = [1,2]
nums2 = [2,3]

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums1.extend(nums2)
    nums1.sort()
    return median(nums1)

print(findMedianSortedArrays(nums1, nums2))
        