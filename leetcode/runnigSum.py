
# 一维数组的动态和
import time
from typing import List


def runningSum(nums: List[int]) -> List[int]:
    sums = []
    s = 0
    for i in nums:
        s += i
        sums.append(s)
    return sums


class Solution:
    pass
        

if __name__ == '__main__':
    l = [1,2,3,4,3,1,2,10,1]
    t1 = time.time()
    print(runningSum(l))
    t2 = time.time()
    print('%0.10f sec' % (t2 - t1))
