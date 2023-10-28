class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n==1:
            return 5
        a=e=i=o=u=1
        mod=10**9+7
        for x in range(2,n+1):
            newa = (e + u + i) % mod
            newe = (a + i) % mod
            newi = (e + o) % mod
            newo = i
            newu = (i + o) % mod
            a,e,i,o,u=newa,newe,newi,newo,newu
        return (a+e+i+o+u)%mod
