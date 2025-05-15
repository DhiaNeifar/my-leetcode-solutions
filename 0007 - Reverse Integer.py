class Solution:
    def reverse(self, x: int) -> int:
        if(x <= 0 ):
            x = - x
            y = 0
            while (x != 0):
                y += (x % 10)
                x //= 10
                y *= 10
            y //= 10
            if (- pow(2, 31) <= y <= pow(2, 31) - 1) :
                return(-y)
            else: 
                return(0)
        else:
            y = 0
            while (x != 0):
                y += (x % 10)
                x //= 10
                y *= 10
            y //= 10
            if (- pow(2, 31) <= y <= pow(2, 31) - 1) :
                return(y)
            else:
                return(0)