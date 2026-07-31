"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head):
        if not head:
            return head
        self.dfs(head)
        return head
    def dfs(self,node):
        curr=node
        last=None
        while curr:
            nxt=curr.next
            if curr.child:
                childlast=self.dfs(curr.child)
                curr.next=curr.child
                curr.child.prev=curr
                curr.child=None
                if nxt:
                    childlast.next=nxt
                    nxt.prev=childlast
                last=childlast
            else:
                last=curr
            curr=nxt
        return last