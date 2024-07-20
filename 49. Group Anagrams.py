"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {} 
        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            result[key] = result.get(key, []) + [s] # Tuple because in python, lists cannot be dict keys
        return result.values()
