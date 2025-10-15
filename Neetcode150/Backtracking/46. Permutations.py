from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Store all permutations
        result = []

        def func(bag=[]):
            # Base case: if current permutation is complete
            if len(bag) == len(nums):
                result.append(bag)
                return

            # Try adding each number from nums that's not already in current permutation
            for num in nums:
                if num not in bag:
                    # Recursively build permutation by adding current number
                    func(bag + [num])

        # Start the recursion with empty bag
        func()
        return result
