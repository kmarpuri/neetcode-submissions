class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums:
            if num in mp:
                mp[num]+=1
            else:
                mp[num]=1
        return sorted(mp, key=mp.__getitem__, reverse=True)[:k]