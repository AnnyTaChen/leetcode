class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ma_lst = []
        ransomNote_lst = list(ransomNote)
        maga_lst = list(magazine)

        for i in range(len(ransomNote_lst)):
            for j in range(len(maga_lst)):
                if ransomNote_lst[i] == maga_lst[j]:
                    ma_lst.append(maga_lst[j])
                    maga_lst.remove(maga_lst[j])
                    break

        return ransomNote_lst == ma_lst
