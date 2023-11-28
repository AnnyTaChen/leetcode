from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            print("nums",nums)
            return [nums]
        
        answer = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            print("n",n )
            for j in self.permute(n):
                print("j",j)
                answer.append([num] + j)
                print("answer",answer)
        
        return answer
