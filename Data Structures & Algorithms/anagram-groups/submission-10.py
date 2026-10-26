class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        base = ord('a') #value 97 for letter a
        result = defaultdict(list) #need a dict to hold all of the sublists which share keys
        for st in strs: #each string in the list of input strings
            count = [0] * 26 #26 spaces for all possible letters
            for ch in st: #character in string
                count[ord(ch) - base] += 1 #add one to the current value of each letter position 
            result[tuple(count)].append(st) #store the freq count as a tuple and append the word which shares count values with the others

        return list(result.values()) #return the dict as a list and space each value as a seperate output