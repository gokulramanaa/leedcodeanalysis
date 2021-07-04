#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_file = {}
        for i, val in enumerate(nums):
            res = (target - val)
            # check if result in key and not duplicate
            if res in map_file and map_file.get(res, -1) != i:
                return sorted([i, map_file.get(res)])
            map_file[val] = i
        
# @lc code=end

