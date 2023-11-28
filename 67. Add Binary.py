class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a, num_b = 0, 0

        # 轉換二進制字符串為十進制數字
        for i in range(len(a)):
            num_a += int(a[i]) * (2 ** (len(a) - 1 - i))
        
        for i in range(len(b)):
            num_b += int(b[i]) * (2 ** (len(b) - 1 - i))

        # 將兩數相加
        result = num_a + num_b

        # 將結果轉為二進制字符串
        binary_result = bin(result)[2:]

        return binary_result
