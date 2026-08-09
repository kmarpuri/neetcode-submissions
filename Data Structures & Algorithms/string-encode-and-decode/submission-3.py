class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string+=str(len(s))+"#"+s
        return string

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        ans = []
        count = 0
        while count < len(s):
            digits=s.index("#", count)
            num=int(s[count:digits])
            ans.append(s[digits+1:num+digits+1])
            count=num+digits+1
        return ans
            







