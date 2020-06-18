class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num_longest_substring=0
        current_longest_substring=[]
        for alpha in s:
            if alpha in current_longest_substring:
                num_longest_substring=max(num_longest_substring,len(current_longest_substring))
                alpha_ind = current_longest_substring.index(alpha)
                current_longest_substring=current_longest_substring[alpha_ind+1:]+[alpha]
            else:
                current_longest_substring.append(alpha)
        return max(num_longest_substring,len(current_longest_substring))

    def lengthOfLongestSubstring_ref(self, s: str) -> int:  ##better solution
        used = {}
        start = maxlength = 0
        for i, v in enumerate(s):
            if v in used and start <= used[v]:
                start = used[v] + 1
            else:
                maxlength = max(maxlength, i - start + 1)
            used[v] = i
        return maxlength

input = "pwwkew"
s=Solution()
print(s.lengthOfLongestSubstring(input))
# print(s.twoSum_ref(nums,target))

'''
Given a string, find the length of the longest substring without repeating characters.
Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
'''