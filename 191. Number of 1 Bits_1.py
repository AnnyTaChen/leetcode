#sol1
class Solution:
    def hammingWeight(self, n: int) -> int:
        n_str = bin(n)[2:]  # 將整數轉為二進制，不然本來>=10的會變成一個字串
        count = 0
        for i in range(len(n_str)):
            if n_str[i] == '1':
                count += 1
        return count
