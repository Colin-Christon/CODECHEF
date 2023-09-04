class Solution:
    def Facti(self,fact:int)->int:
        if(fact==0):
            return 1
        fac=fact
        fact=fact-1
        while(fact>1):
            fac=fac*fact
            fact-=1
        return fac
    def uniquePaths(self, m: int, n: int) -> int:
        m=m-1
        n=n-1
        tot=self.Facti(m+n)
        deno1=self.Facti(m)*self.Facti(n)
        return tot//deno1
        
