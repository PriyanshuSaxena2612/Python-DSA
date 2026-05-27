'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def preOrder(self, root):
        result = []
        if root is None:
            return []
        return [root.data] + self.preOrder(root.left) + self.preOrder(root.right)
