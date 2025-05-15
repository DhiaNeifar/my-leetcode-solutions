class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def create_dicts(_str):
            dict_ = {}
            for element in _str:
                x = dict_.get(element, 0)
                dict_[element] = x + 1
            return dict_
        
        def is_anagram(dict1, dict2):
            if len(dict1) != len(dict2):
                return False
            for element in dict1:
                if dict1[element] != dict2.get(element, 0):
                    return False
            return True
        return is_anagram(create_dicts(s), create_dicts(t))