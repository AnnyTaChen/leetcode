class Solution:
    def countAndSay(self, n: int) -> str:
        count=1
        if n<=1:
            return '1'
        if n==2:
            return '11'
        before = '11'
        for i in range(2,n):
            after=''
            a=1
            for j in range(1,len(before)):
                if before[j]==before[j-1]:
                    a+=1
                else:
                    after+=str(a)+before[j-1]
                    a=1
            after+=str(a)+before[len(before)-1]
            before=after
        return after
