class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        for i in range(1000):
            if 2**i==n:
                return True
                break
                
            else:
                continue
        if i==2**1000:
            return False
