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
        '''Solution 1: Wrong idea'''
        for index1 in range(len(nums)):
            num1= nums[index1]
            try:
                index2 = nums.index(target-num1) # Bug here: same number can be used twice!
            except:
                pass 
            else: 
                return [index1,index2]           
        return "Error: Solution not found"

        '''Solution 2: Wrong idea'''
        for index1 in range(len(nums)):
            num1= nums[index1]
            nums.pop(index1) #Index number changed!
            try:
                index2 = nums.index(target-num1) # Bug here: same number can be used twice!
            except:
                pass 
            else: 
                return [index1,index2]           

        return "Error: Solution not found"

        '''Solution 3: Accepted solution. Time:1656ms'''
        for index1 in range(len(nums)):
            num1= nums[index1]
            nums[index1] = '-' 
            try:
                index2 = nums.index(target-num1) # Bug here: same number can be used twice!
            except:
                pass 
            else: 
                return [index1,index2]           
        return "Error: Solution not found"

        '''Solution 4: Better solution: 560ms'''
        list_shift = 0 #Index1
        for _ in range(len(nums)):
            num1= nums[0]
            nums.pop(0) #Always use first element
            
            try:
                index2 = nums.index(target-num1) # Bug here: same number can be used twice!
            except:
                list_shift+=1    
                pass 
            else: 
                index1 = list_shift
                index2 = index2+list_shift+1
                return [index1,index2]            
        return "Error: Solution not found"

        '''Solution 5: Better solution. Time:428ms'''
        index1 = 0
        for _ in range(len(nums)):
            num1= nums[0]
            nums.pop(0) #Index number changed!
            
            try:
                index2 = nums.index(target-num1) # Bug here: same number can be used twice!
            except:
                index1+=1
                pass 
            else: 
                return [index1,index2+index1+1]           
        return "Error: Solution not found"

