class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = [str(i) for i in range(1, n + 1)]
        result.sort()
        return [int(x) for x in result]