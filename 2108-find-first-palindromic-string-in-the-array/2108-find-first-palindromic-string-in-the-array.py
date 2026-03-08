class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next((s for s in words if s==s[::-1]), "")
        