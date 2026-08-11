class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = {}
        ans = set([])
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1

        for k1, v1 in count.items():
            if v1 == 0:
                continue
            count[k1]-=1
            dupeCount = count
            for k2, v2 in dupeCount.items():
                if v2 != 0:
                    if -k1-k2 == k2 and k2 in dupeCount and dupeCount[k2] < 2:
                        continue
                    elif -k1-k2 in dupeCount and dupeCount[-k1-k2] > 0:
                        ans.add(tuple(sorted([k1, k2, -k1-k2])))

            count[k1]=0        
            
        return [list(t) for t in ans]