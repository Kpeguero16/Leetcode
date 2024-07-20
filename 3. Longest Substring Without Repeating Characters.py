"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
"""
class Solution: # My Solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        left, right = 0,1
        found = {s[left]: 0}
        current = 1
        result = 0
        while right < len(s):
            if s[right] not in found:
                current += 1
                found[s[right]] = 0
                right += 1
            else:
                left+=1
                right = left + 1
                current = 1
                found = {s[left]: 0}
            result = max(result, current)
        return result

  class Solution: # Neetcode's solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
