class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        tab = [ind for ind in range(26)]
        const = ord('a')
        
        for char1, char2 in zip(s1, s2):
            ind1 = ord(char1) - const
            ind2 = ord(char2) - const
            while ind1 != tab[ind1]:
                ind1 = tab[ind1]
            while ind2 != tab[ind2]:
                ind2 = tab[ind2]
            min_ind = min(ind1, ind2)
            max_ind = max(ind1, ind2)
            tab[max_ind] = min_ind

        
        result = []
        
        for char in baseStr:
            ind = ord(char) - const
            while ind != tab[ind]:
                ind = tab[ind]
            result.append(chr(const + ind))
        
        return "".join(result)