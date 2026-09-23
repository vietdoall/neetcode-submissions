class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
        # So sánh với chuỗi đảo ngược
        return filtered == filtered[::-1]