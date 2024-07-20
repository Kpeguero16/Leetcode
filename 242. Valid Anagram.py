"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise. 
An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.
"""

class Solution: #My Solution
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 1: 
            return s == t
        if len(s) != len(t):
            return False
        freqs = {}
        for char in s:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1
        freqt = {}
        for char in t:
            if char in freqt:
                freqt[char] += 1
            else:
                freqt[char] = 1
        for char in freqs:
            if char not in freqt:
                return False
            if freqs[char] != freqt[char]:
                return False
        return True

class Solution: # Neetcode solution
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    countS, countT = {}, {}
    for i in range(len(s)):
      countS[s[i]] = 1 + countS.get(s[i], 0)
      countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
      if countS[c] != countT.get(c, 0):
        return False
    return True

# ALTERNATE SOLUTIONS
class Solution: 
  def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

class Solution: 
  def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
