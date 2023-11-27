class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        } 

        # 如果字符串长度为1，直接返回对应的值
        if len(s) == 1:
            return m[s]

        ans = 0
        for i in range(len(s)-1):
            if s[i] == 'I':
                if s[i+1] == 'V' or s[i+1] == 'X':
                    ans -= m[s[i]]
                else:
                    ans += m[s[i]]
            elif s[i] == 'X':
                if s[i+1] == 'L' or s[i+1] == 'C':
                    ans -= m[s[i]]
                else:
                    ans += m[s[i]]
            elif s[i] == 'C':
                if s[i+1] == 'D' or s[i+1] == 'M':
                    ans -= m[s[i]]
                else:
                    ans += m[s[i]]
            else:
                ans += m[s[i]]

        ans += m[s[-1]]  # 添加最后一个罗马数字的值
        return ans
