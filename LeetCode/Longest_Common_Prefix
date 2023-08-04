class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        d={}
        for x in strs:
            d.setdefault(x,len(x))

        min=32000
        str1=""
        for x in d:
            if(d[x]<min):
                min=d[x]
                str1=x
        j=len(str1)
        test=True
        while(j):
            test=True
            for x in range(len(strs)):
                if(str1!=strs[x][0:len(str1)]):
                    test=False
                    break
            if(test!=True):
                str1=str1[0:j-1]
                j-=1
            else:
                break
        if(test!=True):
            str1=""
        return str1
