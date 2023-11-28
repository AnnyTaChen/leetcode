class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        num_row = []

        for i in range(rowIndex + 1):
            num_row.append([])

            for j in range(i + 1):
                if j == 0 or j == i:
                    num_row[i].append(1)
                else:
                    num_row[i].append(num_row[i-1][j-1] + num_row[i-1][j])

        return num_row[rowIndex]
