class Solution:
    def romanToInt(self, ch: str) -> int:
        n = len(ch)
        sum = 0
        i = 0
        while (i < n):
            if ch[n - i -1] == 'I':
                sum += 1
                i += 1
            elif ch[ n - i - 1] == 'V':
                if( (n - i - 1 )!= 0):
                    if ch[n - i - 2] == 'I':
                        sum += 4
                        i += 2
                    else :
                        sum += 5
                        i += 1
                else:
                    sum += 5
                    i += 1
            elif ch[ n - i - 1] == 'X':
                if( (n - i - 1 )!= 0):
                    if ch[n - i - 2] == 'I':
                        sum += 9
                        i += 2
                    else :
                        sum += 10
                        i += 1
                else:
                    sum += 10
                    i += 1
            elif ch[ n - i - 1] == 'L':
                if( (n - i - 1 )!= 0):
                    if ch[n - i - 2] == 'X':
                        sum += 40
                        i += 2
                    else :
                        sum += 50
                        i += 1
                else:
                    sum += 50
                    i += 1
            elif ch[ n - i - 1] == 'C':
                if( (n - i - 1 )!= 0):
                    if ch[n - i - 2] == 'X':
                        sum += 90
                        i += 2
                    else :
                        sum += 100
                        i += 1
                else:
                    sum += 100
                    i += 1
            elif ch[ n - i - 1] == 'D':
                if( (n - i - 1 )!= 0):
                    if ch[n - i - 2] == 'C':
                        sum += 400
                        i += 2
                    else :
                        sum += 500
                        i += 1
                else:
                    sum += 500
                    i += 1
            elif ch[ n - i - 1] == 'M':
                if( (n - i - 1 )!= 0):
                    if ch[n - i - 2] == 'C':
                        sum += 900
                        i += 2
                    else :
                        sum += 1000
                        i += 1
                else:
                    sum += 1000
                    i += 1
        return(sum)