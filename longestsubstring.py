class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hashmap = {}
        result = 0 
        left = 0
        for right in range(len(s)):
            if s[right] in hashmap and hashmap[s[right]] >= left:
                left = hashmap[s[right]] + 1
            hashmap[s[right]] = right
            result = max(result, right - left +1)
        return result
