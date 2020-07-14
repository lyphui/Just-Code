class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_x=str(x)
        return s_x==s_x[::-1]