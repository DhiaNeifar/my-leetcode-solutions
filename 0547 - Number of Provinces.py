class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        result = [i for i in range(n)]

        for i in range(n - 1):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    x = i
                    while x != result[x]:
                        x = result[x]
                    y = j
                    while y != result[y]:
                        y = result[y]
                    if x != y:
                        result[y] = x

        for i in range(n):
            while result[i] != result[result[i]]:
                result[i] = result[result[i]]
        
        return len(set(result))