class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letter_mapping = {
            1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
            11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R',        19:'S',20: 'T',21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
        }
        list1 = []

        while columnNumber > 0:
            c = columnNumber % 26
            columnNumber = (columnNumber - 1) // 26  # 修正計算方式
            list1.append(letter_mapping[c] if c > 0 else 'Z')

        return ''.join(reversed(list1))#還要記得翻轉
