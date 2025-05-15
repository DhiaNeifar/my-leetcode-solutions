class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        else:
            el = strs[0]
            for i in range(1, len(strs)):
                while not strs[i].startswith(el):
                    el = el[:len(el) - 1]
                    if el == '':
                        return ''
            return el