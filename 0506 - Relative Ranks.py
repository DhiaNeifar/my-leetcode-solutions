class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        results = ['' for _ in range(len(scores))]
        for index, score in enumerate(scores):
            if index == 0:
                results[score[0]] = "Gold Medal"
            elif index == 1:
                results[score[0]] = "Silver Medal"
            elif index == 2:
                results[score[0]] = "Bronze Medal"
            else:
                results[score[0]] = str(index + 1)
        return results