class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0:
            return False

        reverse_number = 0
        
        while reverse_number < x:
            last_digit = x % 10
            reverse_number = reverse_number * 10 + last_digit
            x = x // 10    

        if x == reverse_number:
            return True
        elif x == reverse_number // 10:
            return True
        
        else:
            return False