class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        squares = sum(students)
        circulars = len(students) - squares
        for food in sandwiches:
            if food and squares:
                squares -= 1
            elif not food and circulars:
                circulars -= 1
            else:
                return squares + circulars
        return 0