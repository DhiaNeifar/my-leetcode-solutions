class Solution:
    def trailingZeroes(self, n: int) -> int:
        # TOOK TOO LONG DIDNT WORK!!!!
        # if n <= 1:
            # return 0
        # else:
            # x = 1
            # for i in range (2, n + 1):
                # x *= i
            # a = 0
            # while not x % 10:
                # a += 1
                # x //= 10
            # return a
        
        
        #WORKS BUT NOT OPTIMAL
        # if n < 5:
            # return 0
        # else:
            # a5 = 0
            # for i in range (5, n + 1):
                # x5 = i
                # while not x5 % 5: 
                    # a5 += 1
                    # x5 //= 5
            # return a5
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count