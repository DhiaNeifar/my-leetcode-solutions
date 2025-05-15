class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDict, magazineDict = {}, {}
        for char in ransomNote:
            ransomDict[char] = ransomDict.get(char, 0) + 1
        for char in magazine:
            magazineDict[char] = magazineDict.get(char, 0) + 1
        v = True
        for char in ransomDict:
            if ransomDict[char] > magazineDict.get(char, 0):
                return False 
        return True