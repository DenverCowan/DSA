'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers (a-z)(0-9).
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1 # two pointer technique
        while l < r: # iterates through the string until all characters have been compared
            # the next 2 while loops check to make sure each char is alphanumeric before doing the
            # comparison in the if statement below. if they are not they are skipped over.
            while l < r and not s[l].isalnum():
                l+=1
            while l < r and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower(): # checks for equality from both end of the string
                return False
            # if they are equal then each pointer is moved one position closer to each other
            l +=1
            r -=1
        return True
        '''Time complexity is O(n) with n being the length of the string. this is because you
        are eventually checking every character in the string.'''