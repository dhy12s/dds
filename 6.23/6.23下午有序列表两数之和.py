def twosum(nums, target):
    begin = 0
    end = len(nums) - 1
    while begin < end:
        cur = nums[begin] + nums[end]
        if cur == target:
            begin += 1
            end -= 1
            break
        else:
            if cur < target:
                begin += 1
            else:
                end -= 1
    return [begin, end]
