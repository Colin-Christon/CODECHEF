class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        paren=["(","{","["]
        for x in s:
            if(x in paren):
                stack.append(x)
            else:
                if(not stack):
                    return False
                if((x==")" and stack[-1]=="(" )or
                (x=="}" and stack[-1]=="{") or (x=="]" and stack[-1]=="[") ):
                    stack.pop()
                else:
                    return False
        if(stack):
            return False
        else:
            return True
                
