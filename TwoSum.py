def twoSum(self, nums, target):
        lst=[]
        for i in range(0,len(nums)-1):
            for j in range(0,len(nums)):
                if i != j:
                    if (nums[i] + nums[j]) == target:
                        lst.append(i)
                        lst.append(j)
                        return lst
                
    
            
lst1  = [3,2,4]
twoSum(lst1,6)
