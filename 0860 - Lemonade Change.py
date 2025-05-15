class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {
            5: 0,
            10: 0,
        }
        for bill in bills:
            if bill == 5:
                change[5] = change[5] + 1
            if bill == 10:
                if not change[5]:
                    return False
                change[5] = change[5] - 1
                change[10] = change[10] + 1
            if bill == 20:
                priority = False
                if change[10] and change[5]:
                    priority = True
                    change[10] = change[10] - 1
                    change[5] = change[5] - 1
                if not priority:
                    if change[5] < 3:
                        return False
                    change[5] = change[5] - 3
        return True