class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        not_found=False
        if(len(nums)<3):
            return False
        li=[0]*len(nums)
        li[0]=nums[0]
        stack=[]
        for x in range(1,len(nums)):
            li[x]=min(nums[x],li[x-1])
        for y in range(len(nums)-1,-1,-1):
            if(nums[y]>li[y]):
                while stack and stack[-1]<=li[y]:
                    stack.pop()
                if stack and stack[-1]<nums[y]:
                    return True
                stack.append(nums[y])
        return False
