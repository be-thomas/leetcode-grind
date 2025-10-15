from typing import List


class Solution:
    # Pattern: For each number, we have two choices - include it or not include it (decision tree)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res stores all possible subsets
        res = []
        # subsets stores current subset being built
        subsets = []

        def dfs(i):
            # Base case: when we've processed all numbers
            # Add current subset to result and return
            if i >= len(nums):
                res.append(subsets.copy())
                return

            # Decision 1: Include current number
            subsets.append(nums[i])
            dfs(i + 1)  # Move to next number

            # Decision 2: Don't include current number
            # First remove the number we added
            subsets.pop()
            dfs(i + 1)  # Move to next number without current number

        dfs(0)  # Start from index 0
        return res
