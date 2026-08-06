class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left=0
        mx=0
        count,vowel=0,0
        for right in range (len(s)):
            if s[right] in "aeiou":
                vowel+=1
            if right >=k-1:
                mx=max(mx,vowel)
                if s[left]in "aeiou":
                    vowel-=1
                left=left+1
        return  mx           

        

