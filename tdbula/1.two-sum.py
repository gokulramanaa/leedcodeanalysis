#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            for j, k in enumerate(nums[i+1:]):
                if v + k == target:
                    return [i, j]
        
# @lc code=end

