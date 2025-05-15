class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_freq = {}
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1
        
        order_freq = {}
        for char in order:
            order_freq[char] = order_freq.get(char, 0) + 1
        
        new_string = []
        order_index = 0
        
        for char in s:
            if char not in order_freq:
                new_string.append(char)
            else:
                new_string.append(order[order_index])
                s_freq[order[order_index]] -= 1
                if s_freq[order[order_index]] == 0:
                    order_index += 1

        return "".join(new_string)