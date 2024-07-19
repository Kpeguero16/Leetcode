"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

class Solution: 
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currentSum = 0

        for number in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += number
            maxSub = max(currentSum, maxSub)
        return maxSub
