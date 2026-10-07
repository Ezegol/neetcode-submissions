class Solution:
    def isPalindrome(self, s: str) -> bool:
        data = " ".join(h for h in s if h.isalnum()).lower()

        for i in range(len(data)//2):
            
            if data[i] != data[len(data)-1-i]:
                return False
        return True
        