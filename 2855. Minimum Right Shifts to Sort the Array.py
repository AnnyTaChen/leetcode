
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        count = 0
#nums =[3,4,5,1,2]
#for i in range(len(nums)):
#  nums=nums[-1:]+nums[:-1]#最後一個插入第一個
#  print(nums[-1:])
#\\ [2] [1] [3] [4] [5] 
#  print(nums[:-1])
#-----------------------
#\\[3 4 5 1].......
#  print(nums[-1:]+nums[:-1])
#-----------------------
        if nums == sorted(nums):
            return 0
        for i in range(len(nums)):
            nums = nums[-1:] + nums[:-1] #最後一個插入第一個
            count+=1
            if nums == sorted(nums):
                return count
        return -1
