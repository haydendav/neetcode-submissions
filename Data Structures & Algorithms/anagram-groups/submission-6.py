class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        res = {}
        
        for string in strs:
            key = ''.join(sorted(string)) #make a key by sorting and joining list together
            if key in res:
                res[key].append(string) #if its there add it to the list
            else:
                res[key] = [string] #else create a new list
        
        return list(res.values()) #values gives us the children
                