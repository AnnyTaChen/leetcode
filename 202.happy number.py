class Solution:
    def isHappy(self, n: int) -> bool:
        while n!=1:
            n_str = str(n)
            new_n=0
            for i in range(len(str(n))):
                new_n += int(n_str[i])**2
            n = new_n
            if n == 1:
                return True
            elif n == 4 and n != 1:
                return False
        return True
