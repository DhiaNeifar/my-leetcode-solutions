class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([x[11] for x in details if int(x[11: 13]) > 60])