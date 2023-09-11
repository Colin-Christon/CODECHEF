class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d={}
        for x in range(len(groupSizes)):
            if(groupSizes[x] not in d):
                d.setdefault(groupSizes[x],[])
            d[groupSizes[x]].append(x)
        newlist=[]
        for key in d.keys():
            i=0
            while(i <len(d[key])):
                newlist.append(d[key][i:i+key])
                i=i+key
        return newlist
