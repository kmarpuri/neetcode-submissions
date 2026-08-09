class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        ans = []
        for s in strs:
            sortStr = ''.join(sorted(s))
            if sortStr in anagram:
                ans[anagram[sortStr]].append(s)
            else:
                anagram[sortStr] = len(ans)
                ans.append([s])
        return ans