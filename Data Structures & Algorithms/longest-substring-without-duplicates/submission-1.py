class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        count = 0
        ans = 0
        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[count])
                count+=1
            visited.add(s[i])
            ans = max(ans, i - count + 1)
            
        return ans
            
