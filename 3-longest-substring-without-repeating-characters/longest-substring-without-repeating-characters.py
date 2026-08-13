class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len=0
        left=0
        seen=set()
        for right in range(len(s)):
            ch=s[right]
            while ch in seen:
                seen.remove(s[left])
                left+=1
            seen.add(ch)
            max_len= max(max_len,right-left+1)
        return max_len