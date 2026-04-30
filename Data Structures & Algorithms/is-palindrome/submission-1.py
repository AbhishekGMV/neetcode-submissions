class Solution:
    def isalnum(self, ch):
        return (
            (ord('a') <= ord(ch) <= ord('z')) or
            (ord('A') <= ord(ch) <= ord('Z')) or
            (ord('0') <= ord(ch) <= ord('9'))
        )

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not self.isalnum(s[j]):
                j -= 1

            while i < j and not self.isalnum(s[i]):
                i += 1
            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j-=1

        return True
                
