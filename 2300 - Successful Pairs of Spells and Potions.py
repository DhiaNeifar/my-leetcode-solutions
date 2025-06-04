class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        potions.sort()
        
        for spell in spells:
            first_index = 0
            if spell * potions[-1] >= success:
                new_target = success / spell
                first_index = find_first_index(potions, new_target)
                result.append(len(potions) - first_index)
            else:
                result.append(0)
        
        return result
    
def find_first_index(potions, target):
    start = 0
    end = len(potions) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if potions[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start