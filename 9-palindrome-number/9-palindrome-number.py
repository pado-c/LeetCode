class Solution:
    def isPalindrome(self, x: int) -> bool:
        x =str(x)
        check = ''
        for i in range (len(x)):
            if x[i] == x[-i-1] :
                check += 'O'
        if check == 'O'*len(x):
            return True