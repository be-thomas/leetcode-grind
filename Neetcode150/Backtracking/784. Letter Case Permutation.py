from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def dfs(i, permutation):
            if i >= len(s):
                res.append("".join(permutation))
                return

            if s[i].isdigit():
                dfs(i + 1, permutation + [s[i]])
            else:
                dfs(i + 1, permutation + [s[i].lower()])
                dfs(i + 1, permutation + [s[i].upper()])

        dfs(0, [])
        return res
