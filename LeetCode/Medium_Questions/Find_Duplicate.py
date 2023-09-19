class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        li=[0]*(len(nums)-1)
        for x in nums:
            if(li[x-1]!=0):
                return x
            li[x-1]=1
        
       
