class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if s == t:
            return 0
        dict_1, dict_2 = {}, {}
        for i in range(len(s)):
            if s[i] in dict_1:
                dict_1[s[i]] += 1
            else:
                dict_1[s[i]] = 1
            if t[i] in dict_2:
                dict_2[t[i]] += 1
            else:
                dict_2[t[i]] = 1
        operations = 0
        for key in dict_1:
            operations += min(dict_1[key], dict_2.get(key, 0))
        results = len(s) - operations
        return results