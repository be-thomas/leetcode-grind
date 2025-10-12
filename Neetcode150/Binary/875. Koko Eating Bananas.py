import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min, k_max = 1, max(piles)
        res = k_max
        while k_min < k_max:
            k_optimal = (k_max + k_min) // 2

            required = 0
            for pile in piles:
                required += math.ceil(pile / k_optimal)

            # If required hours is greater than
            # hours given then try smaller
            if required <= h:
                res = k_optimal
                k_max = k_optimal
            else:
                k_min = k_optimal + 1
        return res
