class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        boolean = True
        center = len(num) // 2 + 1
        for i in range(center):
            backward = len(num) - i - 1
            if num[i] != num[backward]:
                return False
        return boolean
