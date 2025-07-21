class Solution:
    def generateTag(self, caption: str) -> str:
        result = ["#"]
        i = 0
        words = caption.split(" ")
        words = [word for word in words if word != ""]
        for ind, word in enumerate(words):
            new_word = []
            for character in word:
                if character.isalpha():
                    new_word.append(character.lower())
            if ind != 0:
                new_word[0] = new_word[0].upper()
                
            result.extend(new_word)
            if len(result) > 100:
                break

        return "".join(result[:100])