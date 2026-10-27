class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} 
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 #for each number update the count of how many appear of each number

        buckets = [[] for _ in range(len(nums) + 1)] #make a list of lists the size of the len + 1

        for num, count in freq.items(): #for each number and freq in freq 
            buckets[count].append(num) #sort each number by how often it happened
            
        result = []

        for i in range(len(buckets) - 1, 0, -1): #starting at len-1, ending at 0(1), and going down by 1
            for number in buckets[i]:
                result.append(number) #for each number in bucket starting at the top append it to the list
                if len(result) == k: #and check if it is the same length as k to return immediately
                    return result

        return result