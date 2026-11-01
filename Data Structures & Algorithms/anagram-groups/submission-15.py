class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            res[(tuple(count))].append(string) # save the string based on tuple which will be the same for anagrams

        return list(res.values())