class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        F=[0 for i in range(n)]
        F[0]=1
        F[1]=2
        for i in range(2,n):
            F[i]=F[i-1]+F[i-2]
        return F[n-1]
