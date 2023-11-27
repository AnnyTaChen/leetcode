class Solution:
    def reverse(self, x: int) -> int:
        #x=123
        #num=0
        #x=12
        #num=3
        #x=1
        #num32
        #x=0
        #num=321
        num=0
        if x < 0:
            is_negative = True
            x = abs(x)
        else:
            is_negative = False
        
        while x != 0:
            T = x % 10
            x = x // 10
            num = num * 10 + T

        if num < -2**31 or num> 2**31 - 1:
            num=0
        else:
            if is_negative:
                num = -num
            else:
                num = num     
        return num

