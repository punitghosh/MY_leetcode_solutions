"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        hashmap={}

        current= head
        
        while current:
            hashmap[current]= Node(current.val)  # Create a completely NEW node with the same value
            current= current.next
        
        current= head

        while current:
            copy= hashmap[current] # Find copy corresponding to  current original node

            # Original current.next
        #        ↓
        #      B
        #
        # hashmap[B]
        #        ↓
        #      B'
        #
        # Therefore:
        # copy.next = B'

            copy.next= hashmap.get(current.next)
            copy.random= hashmap.get(current.random)
            current=current.next                     # Move through ORIGINAL list
        
        return hashmap[head]                          # Return copy of original head

        