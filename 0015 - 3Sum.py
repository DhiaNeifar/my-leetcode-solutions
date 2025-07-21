class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ls=set()
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    ls.add((nums[i],nums[l],nums[r]))
                    l+=1
                elif nums[i]+nums[l]+nums[r]>0: 
                    r-=1
                else:
                    l+=1
        return list(ls)