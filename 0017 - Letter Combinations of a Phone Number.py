class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
    
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r','s'], 
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        if len(digits) == 1:
            return d[digits]

        if len(digits) == 2:
            i, j = digits[0], digits[1]
            combinations = []
            for element_i in d[i]:
                for element_j in d[j]:
                    combinations.append(''.join([element_i, element_j]))
            return combinations
        if len(digits) == 3:
            i, j, k = digits[0], digits[1], digits[2]
            combinations = []
            for element_i in d[i]:
                for element_j in d[j]:
                    for element_k in d[k]:
                        combinations.append(''.join([element_i, element_j, element_k]))
            return combinations
        if len(digits) == 4:
            i, j, k, l = digits[0], digits[1], digits[2], digits[3]
            combinations = []
            for element_i in d[i]:
                for element_j in d[j]:
                    for element_k in d[k]:
                        for element_l in d[l]:
                            combinations.append(''.join([element_i, element_j, element_k, element_l]))
            return combinations