class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time_ = 0
        for i in range(1, len(points)):
            point1 = points[i - 1]
            point2 = points[i]
            a, b = abs(point2[0] - point1[0]), abs(point2[1] - point1[1])
            time_ += max(a, b)
        return time_