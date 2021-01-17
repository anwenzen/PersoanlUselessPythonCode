
# 拥有最多糖果的孩子
from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    maxcandies = max(candies)
    return [candy + extraCandies >= maxcandies for candy in candies]


if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    result = kidsWithCandies(candies=candies, extraCandies=extraCandies)
    print(result)
