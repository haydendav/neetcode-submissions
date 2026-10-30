class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        base = ord('a')

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - base] += 1
            result[tuple(count)].append(string)
        
        return list(result.values())
        