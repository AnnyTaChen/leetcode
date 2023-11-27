class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        b = []
        for i in range(len(nums)):
            if nums[i] not in b:
                b.append(nums[i])
                
        # 在原地修改 nums
        nums[:] = b
        
        return len(b)
