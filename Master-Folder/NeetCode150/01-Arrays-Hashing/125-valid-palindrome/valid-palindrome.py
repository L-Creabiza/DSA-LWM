class Solution:
    def isPalindrome(self, s: str) -> bool:
        drizzy = "".join(char for char in s if char.isalnum()).lower()
        if drizzy == drizzy[::-1]:
            return True
        else:
            return False