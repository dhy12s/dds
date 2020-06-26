# 16. 最接近的三数之和
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 示例：
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
# 提示：
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4

from typing import List


def threeSumClose(nums: List[int], target: int) -> int:
    nums.sort()
    min = abs(nums[0] + nums[1] + nums[2] - target)
    result = nums[0] + nums[1] + nums[2]

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            if abs(sums - target) < min:
                min = abs(sums - target)
                result = sums
            if sums > target:
                right -= 1
            elif sums < target:
                left += 1
            else:
                return sums
    return result


q = [-1, 2, 1, -4]

print(threeSumClose(q,1))
