#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

@author NickZxing
@date 2020/10/28 13:56
"""


def two_sum(nums, target):
    record_dict = {}
    for i in range(len(nums)):
        result = target - nums[i]
        if result in record_dict:
            return [record_dict[result], i]
        record_dict[nums[i]] = i
    return []


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
