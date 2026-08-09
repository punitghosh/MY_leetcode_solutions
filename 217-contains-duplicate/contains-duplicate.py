class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap={}
        for i in nums:
            hashmap[i]= hashmap.get(i,0)+1
        for v in hashmap.values():
            if v>1:
                return True
        return False        
        