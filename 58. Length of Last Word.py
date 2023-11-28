class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1=s.strip(" ")
        s2=s1.split(" ")
        return len(s2[-1])
