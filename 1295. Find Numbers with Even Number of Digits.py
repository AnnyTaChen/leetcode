class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count2 = 0

        for num in nums:
            digit_count = 0
            x = num

            # 計算數字的位數
            while x != 0:
                x = x // 10
                digit_count += 1

            # 判斷位數是否為偶數
            if digit_count % 2 == 0:
                count2 += 1

        return count2
