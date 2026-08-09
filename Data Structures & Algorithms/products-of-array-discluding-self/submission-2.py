class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans=[0]*n
        pre=[0]*n
        post=[0]*n
        for i in range(n):
            if i==0:
                pre[i]=nums[i]
                post[n-1-i]=nums[n-1-i]
            else:
                pre[i]=nums[i]*pre[i-1]
                post[n-1-i]=nums[n-1-i]*post[n-i]
        for i in range(n):
            if i==0 or i==len(nums)-1:
                if i==0 and i==len(nums)-1:
                    ans[i] = 1
                    return ans
                if i==0:
                    ans[i]=post[i+1]
                if i==len(nums)-1:
                    ans[i]=pre[i-1]
            else:
                ans[i]=pre[i-1]*post[i+1]
        return ans


        
            
            
                
