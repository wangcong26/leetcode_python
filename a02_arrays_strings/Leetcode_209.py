from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        Sum = 0
        index = 0
        for i in range(len(nums)):
            Sum += nums[i];
            while Sum >= target:
                res = min(res, i - index + 1)
                Sum -= nums[index]
                index += 1
        return 0 if res==float("inf") else res
if __name__ == '__main__':

    solution = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    print(solution.minSubArrayLen(target, nums))