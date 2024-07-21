"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
class Solution: # My Solution
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        freq = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))
        result = []
        for num in freq:
            result.append(num)
        return result[slice(k)]
