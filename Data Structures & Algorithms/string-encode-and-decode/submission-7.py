class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            res = res + str(len(string)) + "#" + string # concatenate a string with delimeters

        return res

    def decode(self, s: str) -> List[str]:
        i, res = 0, []

        while i < len(s):
            j = i #second pointer if multiple digits
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length]) #append 1 after delimeter to end of string to the result array
            i = j + 1 + length #update i to be the start of the next number

        return res
            