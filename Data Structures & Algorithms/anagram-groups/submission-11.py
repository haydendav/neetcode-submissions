class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        base = ord('a') 
        result = defaultdict(list) 

        for string in strs: 
            freq = [0] * 26 
            for char in string: 
                freq[ord(char) - base] += 1 #increment its position in the alphabet
            result[tuple(freq)].append(string) #append the string by tuple which group them together

        return list(result.values()) #return dict as a list and seperate each value out
        