from typing import List


class Solution:
    def __init__(self, points: List[List[int]]):
        print(self.minTimeToVisitAllPoints(points))

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        move = points[0]
        for i in points[1:]:
            ans += max(abs(move[0]-i[0]), abs(move[1]-i[1]))
            move = i
        return ans


if __name__ == '__main__':
    s = Solution([[1, 1], [3, 4], [-1, 0]])