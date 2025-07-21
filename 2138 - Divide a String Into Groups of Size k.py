class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        div, rest = divmod(len(s), k)
        result = []
        i = 0
        while i < div:
            result.append(s[k * i: k * (i + 1)])
            i += 1
        if rest:
            result.append(s[k * i:] + fill * (k - rest))
        return result