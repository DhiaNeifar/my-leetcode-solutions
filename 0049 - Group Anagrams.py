class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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

        if len(strs) == 1:
            return [strs]

        output = []
        dicts = {}
        for _str in strs:
            dicts[_str] = create_dicts(_str)

        while strs:
            if len(strs) == 1:
                output.append(strs)
                break
            anagrams = [strs[0]]
            new_strs = []
            for i in range(1, len(strs)):
                if is_anagram(dicts[strs[0]], dicts[strs[i]]):
                    anagrams.append(strs[i])
                else:
                    new_strs.append(strs[i])
            output.append(anagrams)
            strs = new_strs
        return output