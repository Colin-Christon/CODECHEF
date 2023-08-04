class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum=0
        i=0
        while(i<len(s)):
            j=i+1
            if(j==len(s)):
                sum+=d[s[i]]
                break
            if(d[s[i]]<d[s[j]]):
                sum=sum+d[s[j]]-d[s[i]]
                i=j+1
            elif(d[s[i]]==d[s[j]]):
                sum=sum+d[s[i]]
                i+=1
            else:
                sum=sum+d[s[i]]
                i+=1
        return sum

