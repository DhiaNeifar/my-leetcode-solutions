from collections import defaultdict, deque

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # Step 1: Bucket words by the first letter they need
        waiting = defaultdict(deque)
        for word in words:
            waiting[word[0]].append((word, 1))  # (word, index of next letter to match)

        count = 0

        # Step 2: Process each character in s
        for char in s:
            # Take all words waiting for this char
            bucket = waiting[char]
            for _ in range(len(bucket)):
                word, idx = bucket.popleft()
                if idx == len(word):
                    count += 1  # fully matched
                else:
                    waiting[word[idx]].append((word, idx + 1))  # move to next needed char

        return count