class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        sCount = dict()
        tCount = dict()

        for ch in s:
            sCount[ch] = sCount.get(ch, 0) + 1

        for ch in t:
            tCount[ch] = tCount.get(ch, 0) + 1

        return sCount == tCount
        