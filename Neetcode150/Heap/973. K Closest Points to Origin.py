import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            x, y = point
            ed = (x**2 + y**2) ** 0.5
            heapq.heappush(h, (ed, point))

        return [heapq.heappop(h)[1] for _ in range(k)]
