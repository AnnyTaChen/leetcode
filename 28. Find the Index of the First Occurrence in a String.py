class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack.count(needle)>0:
            return haystack.find(needle)
        else:
            return -1
