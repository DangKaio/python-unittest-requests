# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-03-21 18:09:55
# @Last Modified time: 2019-07-04 19:23:54


class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(0, len(nums) - 1):
                if nums[i] + nums[j] == target:
                    print("%d %d " % (nums[i], nums[j]))


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 7, 11, 15]
    # print(len(nums))
    sol.twoSum(nums, 9)
