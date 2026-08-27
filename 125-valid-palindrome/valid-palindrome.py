class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string=""
        for i in s:
             if i.isalnum():
                new_string+=i.lower()
        print(new_string)
        return new_string==new_string[::-1]        

        