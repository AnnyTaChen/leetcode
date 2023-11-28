class Solution:
    def isPalindrome(self, s: str) -> bool:
        pakin = []
        for i in range(len(s)):
            if s[i].isalnum():
                pakin.append(s[i].lower())

        if pakin == pakin[::-1]:
            return True
        else:
            return False
