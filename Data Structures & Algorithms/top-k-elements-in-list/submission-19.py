class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        res = []

        for value, frequency in freq.items():
            buckets[frequency].append(value)

        for i in range(len(buckets) - 1, 0, -1):
            for value in buckets[i]:
                res.append(value)
                if len(res) == k:
                    return res