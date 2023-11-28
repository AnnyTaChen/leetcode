class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        min_1 = min(nums)
        max_1 = max(nums)
        nums = set(nums)
        if len(nums) == 1 and min_1 > 0 :
            return min_1 -1
        elif len(nums) == 1 and min_1 == 0:
            return min_1 + 1
        
        for i in range(0, max_1 + 1):
            if i not in nums:
                return i
        return max_1 + 1 #如果都沒少要回傳最大值
