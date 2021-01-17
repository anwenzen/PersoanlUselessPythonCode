# 好数对的数目
from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    num = 0
    for i in range(len(nums)):
        for j in nums[i+1:]:
            if nums[i] == j:
                num += 1
    return num


if __name__ == '__main__':
    nums = [1,1,1,1]
    num = numIdenticalPairs(nums)
    print(num)
