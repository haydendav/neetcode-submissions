class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} #frequency map of how often each number is found

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums)+1)] #create an empty bucket for each space in the len of nums + 1

        for num, count in freq.items(): #get the key and value from map
            buckets[count].append(num) #save the num based on how often it showed up

        res = []

        for i in range(len(buckets) - 1, 0, -1): #start at len of buckets - 1 going down excluding 0
            for num in buckets[i]:
                res.append(num) #append highest freq
                if len(res) == k: #until len equals k
                    return res 