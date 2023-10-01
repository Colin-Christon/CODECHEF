class Solution:
    def reverseWords(self, s: str) -> str:
        li=s.split(" ")
        for x in range(len(li)):
            li[x]=self.palin(li[x])
        print(*li)
        return " ".join(li)
    def palin(self,s:str)->str:
        i=len(s)-1
        s2=""
        for i in range(len(s)-1,-1,-1):
            s2+=s[i]
        return s2
        
