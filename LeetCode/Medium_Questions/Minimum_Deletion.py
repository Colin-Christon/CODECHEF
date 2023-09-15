class Solution:
    def minDeletions(self, s: str) -> int:
        d={}
        for x in s:
          if(x not in d):
            d.setdefault(x,0)
          d[x]+=1
        li=list(d.values())
        li.sort(reverse=True)
        count=0
        print(li)
        while(li!=None):
          temp=li[0]
          if(len(li)==1 or temp==0):
            break
          li.remove(temp)
          while(temp in li):
            index=li.index(temp)
            li[index]-=1
            count+=1
            
        return count
