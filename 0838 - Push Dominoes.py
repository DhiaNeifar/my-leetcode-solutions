class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        if len(dominoes) < 2:
            return dominoes
        def update(old_state):
            new_state = []
            for index, char in enumerate(old_state):
                new_char = char
                if char == '.':
                    if (index == len(dominoes) - 1 and old_state[index - 1] == 'R') or (0 < index and old_state[index - 1] == "R") and (index < len(old_state) - 1 and old_state[index+ 1] != 'L'):
                        new_char = 'R'
                    if (index == 0 and old_state[index + 1] == 'L') or (0 < index and old_state[index - 1] != "R") and (index < len(old_state) - 1 and old_state[index + 1] == 'L'):
                        new_char = 'L'
                new_state.append(new_char)
            return "".join(new_state)
        new_dominoes = update(dominoes)
        while dominoes != new_dominoes:
            dominoes = new_dominoes
            new_dominoes = update(dominoes)
        return new_dominoes