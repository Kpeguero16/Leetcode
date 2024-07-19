class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            visited_numbers = {}
            for index, number in enumerate(nums):
                difference = target - number
                if difference in visited_numbers:
                    return [visited_numbers[difference], index]
                else: 
                    visited_numbers[number] = index
            return
