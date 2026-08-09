class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i,num in enumerate(numbers):
            diff= target-num
            if diff in seen:
                return [seen[diff],i+1]
            seen[num]=i+1
        return []    