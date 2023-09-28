class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenli=[]
        oddli=[]
        for x in nums:
            if(x&1):
                oddli.append(x)
            else:
                evenli.append(x)
        oddli.sort()
        evenli.sort()
        return evenli+oddli
