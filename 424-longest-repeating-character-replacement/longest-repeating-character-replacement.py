class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left=0
        max_freq=0
        count={}
        result=0
        for right in range(len(s)):
            ch=s[right]
            count[ch]=count.get(ch,0)+1
            max_freq= max(max_freq,count[ch])
            while (right-left+1)- max_freq > k:
                count[s[left]] -=1
                left+=1
            result= max(result,right-left+1)
        return result
