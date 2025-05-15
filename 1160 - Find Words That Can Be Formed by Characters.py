class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def return_freq(word_):
            freq_ = {}
            for char_ in word_:
                freq_[char_] = freq_.get(char_, 0) + 1
            return freq_
        
        def check(dict1, dict2):
            for key, value in dict1.items():
                x = dict2.get(key, 0)
                if not (x and value <= x):
                    return False
            return True
        count = 0
        freq = return_freq(chars)
        for word in words:
            word_freq = return_freq(word)
            if check(word_freq, freq):
                count += len(word)
        return count