from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows, n_cols = len(matrix), len(matrix[0])
        low = 0
        high = (n_rows * n_cols) - 1
        while low <= high:
            mid = (low + high) // 2
            item = matrix[mid // n_cols][mid % n_cols]
            if item < target:
                low = mid + 1
            elif item > target:
                high = mid - 1
            else:
                return True
        return False
