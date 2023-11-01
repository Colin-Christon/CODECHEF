# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d={}
        d=self.findNode(root,d)
        minn=1
        li=[]
        for x in d.keys():
            if(minn<d[x]):
                minn=d[x]
        for x in d.keys():
            if(minn==d[x]):
                li.append(x)
            

        return li
    
    def findNode(self,root,d):
        if root==None:
            return d
        if(root.val not in d):
            d.setdefault(root.val,0)
        d[root.val]+=1
        d=self.findNode(root.left,d)
        d=self.findNode(root.right,d)
        return d

