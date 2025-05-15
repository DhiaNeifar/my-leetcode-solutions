class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if word_search(word, 0, board, n, m, [(i, j)]):
                        return True
        return False
    
def find_neighbors(n, m, used):
    x, y = used[-1]
    neighbors = []
    if x - 1 >= 0 and (x - 1, y) not in used:
        neighbors.append((x - 1, y))
    if x + 1 < n and (x + 1, y) not in used:
        neighbors.append((x + 1, y))
    if y - 1 >= 0 and (x, y - 1) not in used:
        neighbors.append((x, y - 1))
    if y + 1 < m and (x, y + 1) not in used:
        neighbors.append((x, y + 1))
    return neighbors
    
def word_search(word, word_index, board, n, m, used):
    if word_index == len(word) - 1:
        return True
    for neighbor in find_neighbors(n, m, used):
        x, y = neighbor
        if board[x][y] == word[word_index + 1]:
            used.append((x, y))
            if word_search(word, word_index + 1, board, n, m, used):
                return True
            used.pop()
    return False