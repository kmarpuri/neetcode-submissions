class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = {}
        ans = 0
        l = 0
        for r in range(len(s)):
            letters[s[r]] = 1 + letters.get(s[r], 0)
            
            while r-l+1-max(letters.values()) > k:
                letters[s[l]]-=1
                l+=1
            ans = max(ans, r-l+1)

        return ans

