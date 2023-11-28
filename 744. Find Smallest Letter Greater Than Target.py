class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        str_ord = []
        
        for i in range(len(letters)):
            str_ord.append(ord(letters[i]))
        
        str_ord = sorted(str_ord)
        
        for i in range(len(str_ord)):
            if str_ord[i] > ord(target):
                return chr(str_ord[i])

        return chr(str_ord[0])
