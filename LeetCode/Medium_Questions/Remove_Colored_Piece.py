class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n=len(colors)
        cnta=0
        cntb=0
        for x in range(1,n-1):
            if(colors[x-1]=="A" and colors[x]=="A" and colors[x+1]=="A"):cnta+=1
            elif(colors[x-1]=="B" and colors[x]=="B" and colors[x+1]=="B"):cntb+=1
        return cnta>cntb
