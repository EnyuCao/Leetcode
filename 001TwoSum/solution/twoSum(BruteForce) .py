#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
#Example:

#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''Solution 6: without list methods: much slower! time: 5424ms''' 
        for index1 in range(len(nums)):
            for index2 in range(index1+1,len(nums),1)
            num1= nums[index1]
            if nums[index1]+nums[index2]==target:
                return [index1,index2]           
        return "Error: Solution not found"

