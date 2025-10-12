from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            # Means we are in the sorted array
            # but we are not entirely sure to do
            # high = mid - 1 as mid can also be the minimum
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
        return nums[low]
