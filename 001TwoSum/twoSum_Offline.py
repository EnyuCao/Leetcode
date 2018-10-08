# Local Test Template
# Manually input
while True:
    try:
        #input_str = raw_input()
#
# Input:
#
        nums =  [3,2,4]#[2, 7, 11, 15]        
        target = 6#9       
        print nums,target

#
# Content:
#

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1 in range(len(nums)):
            for index2 in range(index1+1,len(nums),1):
                if nums[index1]+nums[index2]==target:
                    print [index1,index2]   
        

#
# Finish
#
        print "Finished"
        break
    except:
        break

