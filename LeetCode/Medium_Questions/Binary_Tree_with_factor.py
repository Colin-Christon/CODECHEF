class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        Mod=10**9+7
        arr.sort()
        dp=[1]*len(arr)
        index={}
        for i ,x in enumerate(arr):
            index.setdefault(x,i)
        for i ,num in enumerate(arr):
            for j in range(i):
                if num%arr[j]==0:
                    div=num//arr[j]
                    if div in index:
                        dp[i]+=dp[j]*dp[index[div]]
                        dp[i]%=Mod
        return sum(dp)%Mod
