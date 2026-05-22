class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars, chart = {}, {}

        for i in range(len(s)):
            chars[s[i]] = 1 + chars.get(s[i], 0)
            chart[t[i]] = 1 + chart.get(t[i], 0)

        return chars == chart
