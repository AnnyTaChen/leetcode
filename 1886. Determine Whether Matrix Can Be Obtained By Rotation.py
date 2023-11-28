from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        return self.find_r(mat, target, 0)

    def find_r(self, mat: List[List[int]], target: List[List[int]], rotation_count: int) -> bool:
        if rotation_count > 3:
            return False
        m = len(mat)
        a = [[0] * m for _ in range(m)]
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                a[i][j]=mat[m - j - 1][i]
                if target[i][j] == mat[m - j - 1][i]:
                    count += 0
                else:
                    count += 1
        if count == 0:
            return True
        else:
            rotation_count += 1  # Corrected incrementation
            return self.find_r(a, target, rotation_count)
