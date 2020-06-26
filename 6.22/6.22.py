# # 错误思路
# # l1 = [2,2,3,4,5,6.23,7]
# # for i in range(len(l1)):
# #     l1[i] = l1[i]/l1[0]
# # print(l1)
# # print('------------')
# # # 正确思路
# # l2 = [2,2,3,4,5,6.23,7]
# # for i in range(len(l2)-1,-1,-1):
# #     l2[i] = l2[i] / l2[0]
# # print(l2)

# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# #
# # 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

from typing import List
class Solution1:
    def removeDuplicated(self,nums : List[int]) -> int:
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow +=1
                nums[slow] = nums[fast]
                fast += 1
        return  slow + 1