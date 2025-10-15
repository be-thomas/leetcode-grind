from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # First sort it so that duplicates are adjacent
        nums.sort()

        res = []
        subsets = []

        def dfs(i):
            # Base case
            # When we've processed all numbers
            # then return the current subset
            if i >= len(nums):
                res.append(subsets.copy())
                return

            # Append the current value
            subsets.append(nums[i])
            dfs(i + 1)

            # Backtrack - remove the last added value
            subsets.pop()
            # Skip all duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # After popping, we move to the next non-duplicate element
            # then append the value again
            dfs(i + 1)

        dfs(0)
        return res
