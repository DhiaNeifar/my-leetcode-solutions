class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        length = len(s)
        
        if length < 10:
            return []
        
        d = {}
        for i in range(length - 9):
            seq = s[i: i + 10]
            if seq in d:
                d[seq] += 1
            else:
                d[seq] = 0
        
        return [x for x in d if d[x]]