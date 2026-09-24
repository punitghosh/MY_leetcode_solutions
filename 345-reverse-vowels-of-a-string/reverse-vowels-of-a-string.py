class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=set("aeiouAEIOU")
        s_list = list(s)
        i=0
        j= len(s)-1
        while(i<j):
            while i<j and s_list[i] not in vowel:
                i=i+1
            while i<j and s_list[j] not in vowel:
                j=j-1
           
            s_list[i],s_list[j]=s_list[j],s_list[i]
            i=i+1
            j=j-1
        return "".join(s_list)