from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # List to store all valid combinations
        out = []

        def func(i, bag=[], remaining_capacity=target):
            # Base case: when we've found a valid combination that sums to target
            if remaining_capacity == 0:
                out.append(bag)
                return

            # Edge cases: when index is negative or remaining sum becomes negative
            if i < 0 or remaining_capacity < 0:
                return

            # Current number we're considering
            num = candidates[i]

            # If current number is less than or equal to remaining sum
            # Include the current number and try again with same index
            # (because we can reuse numbers)
            if num <= remaining_capacity:
                func(i, bag + [num], remaining_capacity - num)

            # Skip current number and move to next index
            func(i - 1, bag, remaining_capacity)

        # Start recursion from last index
        func(i=len(candidates) - 1)
        return out
