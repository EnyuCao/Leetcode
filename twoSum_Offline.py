# Local Test Template
# Manually input
while True:
    try:
        #input_str = raw_input()
#
# Input:
#
        nums =  [2, 7, 11, 15]        
        target = 9       
        print nums,target

#
# Content:
#
        
        sort_nums = list(nums) #nums(:)
        print sort_nums
        #sort_nums#.sort()
        nums_len = len(sort_nums)
        result = list()
        for i in range(nums_len):
            for j in range(nums_len-i-1):
                j = j+i+1
                if sort_nums[i]+sort_nums[j]==target:
                    #result.append(nums.index(sort_nums[i]))
                    result.append(i)
                    nums.remove(sort_nums[i])
                    #result.append(nums.index(sort_nums[j])+1)
                    result.append(j)
                    #nums.remove(sort_nums[j])
                    print result
                    
            print "ERROR"
        print "Finished"
    except:
        break

