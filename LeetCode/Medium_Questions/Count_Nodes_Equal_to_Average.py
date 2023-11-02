# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        li=self.findCount(root,[0,0,0])
        print(*li)
        return li[2]

    def findCount(self,root,li):
        lleft=copy.copy(li)
        lright=copy.copy(li)
        if root==None:
            return [0,0,0]
        li2=self.findCount(root.left,lleft)
        li3=self.findCount(root.right,lright)
        li[0]=li2[0]+li3[0]+1
        li[1]=li2[1]+li3[1]+root.val
        li[2]=li2[2]+li3[2]
        av=(li[1])//(li[0])
        if(av==root.val):
            li[2]+=1
        print(*li ,"for node "+str(root.val))
        return li

            
