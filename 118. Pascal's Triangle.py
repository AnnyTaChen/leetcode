class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        nums = [[1]]  
        
        for i in range(1, numRows):#1.1num[1][?]開始
            row = [1]#1.2num[1][1]
            for j in range(1, i):
                row.append(nums[i-1][j-1] + nums[i-1][j])
            row.append(1)
            nums.append(row)
        
        return nums
