class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_symmetry_string(start,end):
            mid=(end-start)//2
            for i in range(mid):
                if s[start+i]!=s[end-i-1]:return False
            return True

        length=len(s)
        num_longest_pldm=0
        longest_pldm=None
        if length<=1:return s
        for i in range(length):
            if i+num_longest_pldm>length:break
            for j in range(length-1,i+num_longest_pldm,-1):
                print(s[i:j])
                if is_symmetry_string(i,j):
                    num_longest_pldm=j-i
                    longest_pldm=s[i:j]
                    break
        return longest_pldm,num_longest_pldm


s=Solution()
print(s.longestPalindrome('cbabd'))



'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''