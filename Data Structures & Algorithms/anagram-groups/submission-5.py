class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return None
        
        res = {}
        
        for string in strs:
            key = ''.join(sorted(string))
            if key in res:
                res[key].append(string)
            else:
                res[key] = [string]
        
        return list(res.values())
                