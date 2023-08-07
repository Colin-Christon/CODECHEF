class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        else:
            a=x
            b=0
            while(x!=0):
                temp=x%10
                b=b*10+temp
                x=x//10
            if(a==b):
                return True 
            else:
                return False
                
