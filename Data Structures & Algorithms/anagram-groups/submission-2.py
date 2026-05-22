class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        master = {}

        for char in strs:
            key = ''.join(sorted(char))
            if key in master:
                master[key].append(char)
            else:
                master[key] = [char]
        return list(master.values())
        