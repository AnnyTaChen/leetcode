class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(2147395599):
            if i*i==x:
                return i
            elif i*i>x:
                i = i - 1
                return i
                break
