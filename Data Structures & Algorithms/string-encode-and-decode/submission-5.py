class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string #concatenate len of string + # + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s): 
            j = i
            while s[j] != "#": #iterate through s until the character after #
                j += 1
            length = int(s[i:j]) #find the length of the string
            res.append(s[j + 1 : j + 1 + length]) #append the string which starts at j+1 and ends at j+1+length
            i = j + 1 + length #update new position at string length + the position of j + the pound
        return res