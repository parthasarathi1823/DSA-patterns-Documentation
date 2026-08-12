class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ans = 0
        num = x
        while x != 0:
            ans=ans*10+(x%10)
            x=x//10
        return ans == num